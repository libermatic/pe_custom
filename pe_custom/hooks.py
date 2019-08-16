# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__

app_name = "pe_custom"
app_version = __version__
app_title = "PE Customization"
app_publisher = "libermatic."
app_description = "Customizations for PE"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@libermatic.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pe_custom/css/pe_custom.css"
# app_include_js = "/assets/pe_custom/js/pe_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/pe_custom/css/pe_custom.css"
# web_include_js = "/assets/pe_custom/js/pe_custom.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pe_custom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pe_custom.install.before_install"
# after_install = "pe_custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pe_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pe_custom.tasks.all"
# 	],
# 	"daily": [
# 		"pe_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"pe_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pe_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pe_custom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pe_custom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pe_custom.event.get_events"
# }
