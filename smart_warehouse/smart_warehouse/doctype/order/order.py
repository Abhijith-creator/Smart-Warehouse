# Copyright (c) 2025, Abhijith and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class Order(Document):
    def validate(self):
        if self.quantity <= 0:
            frappe.throw("Quantity must be greater than zero")
