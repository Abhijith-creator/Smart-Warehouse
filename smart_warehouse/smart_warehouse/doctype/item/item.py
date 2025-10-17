import frappe
from frappe.model.document import Document

class Item(Document):
    def validate(self):
        if self.quantity < 0:
            frappe.throw("Quantity cannot be negative")
