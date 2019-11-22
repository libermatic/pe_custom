# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": "Data",
            "items": [
                {"type": "doctype", "name": "Yum Import", "label": _("Yum Import")}
            ],
        },
        {
            "label": "Setup",
            "items": [
                {
                    "type": "doctype",
                    "name": "PE Custom Settings",
                    "label": _("PE Custom Settings"),
                }
            ],
        },
    ]
