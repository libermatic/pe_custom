# -*- coding: utf-8 -*-
# Copyright (c) 2019, libermatic. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe.model.document import Document
from frappe.utils.xlsxutils import read_xlsx_file_from_attached_file
from frappe.utils.csvutils import read_csv_content
from functools import partial
from toolz import compose, drop, excepts, first


class YumImport(Document):
    def before_save(self):
        row_count = compose(lambda x: len(x[1]), _get_data)
        self.customers_imported = row_count(self.customers)
        self.items_imported = row_count(self.items)
        self.sales_imported = row_count(self.sales)

    def before_submit(self):
        if not self.sales_imported:
            frappe.throw(frappe._("No <strong>Sales</strong> to import."))

    def on_submit(self):
        customers = _create_customers(self.customers)
        if customers:
            frappe.db.set_value(
                self.doctype, self.name, "customers_created", len(customers)
            )


def _get_data(file_url):
    get_header = excepts(StopIteration, first, lambda _: [])
    get_rows = compose(list, partial(drop, 1))
    if not file_url:
        return [], []

    file = frappe.get_doc("File", {"file_url": file_url})
    filename, file_extension = file.get_extension()
    if file_extension == ".xlsx":
        data = read_xlsx_file_from_attached_file(file_url=file_url)
        return get_header(data), get_rows(data)
    if file_extension == ".csv":
        data = read_csv_content(file.get_content())
        return get_header(data), get_rows(data)
    frappe.throw(frappe._("Unsupported File Format"))


def _create_customers(file_url):
    headers, rows = _get_data(file_url)
    if not headers:
        return []
    fields = {
        "Customer ID": 1,
        "Customer Name": 2,
        "Phone Number": 3,
        "Gender": 4,
        "Birthday": 5,
        "Anniversary": 6,
        "Source": 13,
    }
    if not _has_valid_headers(headers, fields):
        frappe.throw(frappe._("Invalid <strong>Customer</strong> data format."))

    customer_group, territory = frappe.db.get_value(
        "Selling Settings", None, ["customer_group", "territory"]
    )

    def create(row):
        customer = frappe.get_doc(
            {
                "doctype": "Customer",
                "customer_name": row[fields.get("Customer Name")],
                "gender": row[fields.get("Gender")],
                "type": "Individual",
                "pe_yum_customer_ref": row[fields.get("Customer ID")],
                "customer_group": customer_group,
                "territory": territory,
                "pe_source": row[fields.get("Source")],
                "pe_customer_birthday": row[fields.get("Birthday")],
                "pe_customer_anniversary": row[fields.get("Anniversary")],
            }
        ).insert(ignore_user_permissions=True)
        contact = frappe.get_doc(
            {
                "doctype": "Contact",
                "first_name": "Self",
                "gender": row[fields.get("Gender")],
                "phone_nos": [
                    {"phone": row[fields.get("Phone Number"), "is_primary_mobile_no":1]}
                ],
                "is_primary_contact": 1,
                "links": [{"link_doctype": "Customer", "link_name": customer.name}],
            }
        ).insert(ignore_user_permissions=True)
        customer.customer_primary_contact = contact.name
        customer.save(ignore_user_permissions=True)
        return customer

    return [
        create(x)
        for x in filter(
            lambda x: not frappe.db.exists(
                "Customer", {"pe_yum_customer_ref": x[fields.get("Customer ID")]}
            ),
            rows,
        )
    ]


def _has_valid_headers(headers, fields):
    try:
        for fieldname, idx in fields.items():
            if headers[idx] != fieldname:
                return False
    except IndexError:
        return False
    return True
