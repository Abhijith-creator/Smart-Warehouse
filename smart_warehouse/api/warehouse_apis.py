import frappe


# ==============================
#  ITEM MANAGEMENT APIS
# ==============================

@frappe.whitelist(allow_guest=True)
def create_item():
    try:
        data = frappe.local.form_dict
        required_fields = ["item_code", "item_name"]
        missing = [f for f in required_fields if not data.get(f)]
        if missing:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"Missing required fields: {', '.join(missing)}",
                "error": True
            })
            return

        if frappe.db.exists("Item", {"item_code": data.get("item_code")}):
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"Item {data.get('item_code')} already exists",
                "error": True
            })
            return

        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": data.get("item_code"),
            "item_name": data.get("item_name"),
            "quantity": data.get("quantity") or 0,
            "location": data.get("location") or ""
        })
        item.insert(ignore_permissions=True)
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": f"Item {item.item_code} created successfully"
        })
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(frappe.get_traceback(), "Create Item API Error")
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


@frappe.whitelist(allow_guest=True)
def get_item(item_code=None):
    try:
        if not item_code:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": "Missing item_code",
                "error": True
            })
            return

        item = frappe.get_doc("Item", {"item_code": item_code})
        frappe.local.response.update({
            "http_status_code": 200,
            "item_code": item.item_code,
            "item_name": item.item_name,
            "quantity": item.quantity,
            "location": item.location
        })
    except frappe.DoesNotExistError:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": f"Item {item_code} not found",
            "error": True
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


@frappe.whitelist(allow_guest=True)
def update_item(item_code=None, quantity=None, location=None):
    try:
        if not item_code:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": "Missing item_code",
                "error": True
            })
            return

        item = frappe.get_doc("Item", {"item_code": item_code})
        if quantity is not None:
            item.quantity = int(quantity)
        if location is not None:
            item.location = location
        item.save(ignore_permissions=True)
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": f"Item {item_code} updated successfully"
        })
    except frappe.DoesNotExistError:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": f"Item {item_code} not found",
            "error": True
        })
    except Exception as e:
        frappe.db.rollback()
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


@frappe.whitelist(allow_guest=True)
def delete_item(item_code=None):
    try:
        if not item_code:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": "Missing item_code",
                "error": True
            })
            return

        frappe.delete_doc("Item", {"item_code": item_code}, ignore_permissions=True)
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": f"Item {item_code} deleted successfully"
        })
    except frappe.DoesNotExistError:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": f"Item {item_code} not found",
            "error": True
        })
    except Exception as e:
        frappe.db.rollback()
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


# ==============================
#  ORDER MANAGEMENT APIS
# ==============================

@frappe.whitelist(allow_guest=True)
def create_order():
    try:
        data = frappe.local.form_dict
        required_fields = ["order_id", "customer_name", "item", "quantity"]
        missing = [f for f in required_fields if not data.get(f)]
        if missing:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"Missing required fields: {', '.join(missing)}",
                "error": True
            })
            return

        if frappe.db.exists("Order", {"order_id": data.get("order_id")}):
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"Order {data.get('order_id')} already exists",
                "error": True
            })
            return

        order = frappe.get_doc({
            "doctype": "Order",
            "order_id": data.get("order_id"),
            "customer_name": data.get("customer_name"),
            "item": data.get("item"),
            "quantity": data.get("quantity"),
            "status": "Pending"
        })
        order.insert(ignore_permissions=True)
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": f"Order {order.order_id} created successfully"
        })
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(frappe.get_traceback(), "Create Order API Error")
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


@frappe.whitelist(allow_guest=True)
def update_order_status():
    try:
        data = frappe.local.form_dict
        order_id = data.get("order_id")
        status = data.get("status")

        if not order_id or not status:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": "Missing order_id or status",
                "error": True
            })
            return

        order = frappe.get_doc("Order", {"order_id": order_id})
        order.status = status
        order.save(ignore_permissions=True)
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": f"Order {order_id} status updated to {status}"
        })
    except frappe.DoesNotExistError:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": f"Order {order_id} not found",
            "error": True
        })
    except Exception as e:
        frappe.db.rollback()
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


@frappe.whitelist(allow_guest=True)
def list_orders():
    try:
        orders = frappe.get_all("Order", fields=["order_id", "customer_name", "item", "quantity", "status"])
        frappe.local.response.update({
            "http_status_code": 200,
            "orders": orders
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


# ==============================
#  WAREHOUSE USER APIS
# ==============================

@frappe.whitelist(allow_guest=True)
def create_warehouse_user():
    try:
        data = frappe.local.form_dict
        required_fields = ["full_name", "email"]
        missing = [f for f in required_fields if not data.get(f)]
        if missing:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"Missing required fields: {', '.join(missing)}",
                "error": True
            })
            return

        if frappe.db.exists("Warehouse User", {"email": data.get("email")}):
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"User with email {data.get('email')} already exists",
                "error": True
            })
            return

        user = frappe.get_doc({
            "doctype": "Warehouse User",
            "full_name": data.get("full_name"),
            "email": data.get("email"),
            "role": data.get("role", "Staff"),
            "phone_number": data.get("phone_number")
        })
        user.insert(ignore_permissions=True)
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": f"User {user.full_name} created successfully"
        })
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(frappe.get_traceback(), "Create Warehouse User API Error")
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


@frappe.whitelist(allow_guest=True)
def list_warehouse_users():
    try:
        users = frappe.get_all("Warehouse User", fields=["full_name", "email", "role", "phone_number"])
        frappe.local.response.update({
            "http_status_code": 200,
            "users": users
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


# ==============================
#  SCAN LOG APIS
# ==============================

@frappe.whitelist(allow_guest=True)
def log_scan():
    try:
        data = frappe.local.form_dict
        required_fields = ["item", "scanned_by"]
        missing = [f for f in required_fields if not data.get(f)]
        if missing:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"Missing required fields: {', '.join(missing)}",
                "error": True
            })
            return

        scan = frappe.get_doc({
            "doctype": "Scan Log",
            "item": data.get("item"),
            "scanned_by": data.get("scanned_by"),
            "scan_type": data.get("scan_type", "Inward"),
            "remarks": data.get("remarks")
        })
        scan.insert(ignore_permissions=True)
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": f"Scan logged for item {scan.item}"
        })
    except Exception as e:
        frappe.db.rollback()
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })


@frappe.whitelist(allow_guest=True)
def get_scan_history():
    try:
        item = frappe.local.form_dict.get("item")
        if not item:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": "Missing item parameter",
                "error": True
            })
            return

        logs = frappe.get_all("Scan Log",
                              filters={"item": item},
                              fields=["item", "scanned_by", "scan_time", "scan_type", "remarks"])
        if not logs:
            frappe.local.response.update({
                "http_status_code": 400,
                "message": f"No scan logs found for item {item}",
                "error": True
            })
            return

        frappe.local.response.update({
            "http_status_code": 200,
            "logs": logs
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "message": str(e),
            "error": True
        })
