# Copyright (c) 2025, Abhijith and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class WarehouseUser(Document):
    def validate(self):
        if not self.email:
            frappe.msgprint("Warning: Email not provided for user.")
