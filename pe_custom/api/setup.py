# -*- coding: utf-8 -*-
# Copyright (c) 2019, libermatic. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe


@frappe.whitelist()
def setup_defaults():
    _update_settings()


def _update_settings():
    def update(doctype, params):
        doc = frappe.get_single(doctype)
        doc.update(params)
        doc.save(ignore_permissions=True)

    settings = {
        "Selling Settings": {"cust_master_name": "Naming Series"},
        "Stock Settings": {"item_naming_by": "Naming Series"},
    }

    return [update(*x) for x in settings.items()]
