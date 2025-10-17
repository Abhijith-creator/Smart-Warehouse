# Copyright (c) 2025, Abhijith and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime

class ScanLog(Document):
    def before_insert(self):
        if not self.scan_time:
            self.scan_time = now_datetime()
