# Smart Warehouse Management System

A **Frappe** app for managing warehouse items, orders, users, and scan logs via APIs.  



## ℹ️ About

The **Smart Warehouse Management System** is a Frappe-based application designed to simplify warehouse operations.  
It allows warehouse staff and managers to:

- Track inventory items with details like code, name, quantity, and location.  
- Manage orders, including creation, status updates, and viewing order history.  
- Maintain warehouse user accounts with roles and contact details.  
- Log item scans for inward and outward movements and review scan history.  

The system is API-driven, making it easy to integrate with other applications or front-end interfaces.  
It provides clear responses for both successful operations and error cases, ensuring smooth automation and monitoring of warehouse activities.

## 🚀 Features

- **Inventory Management**: Track items with code, name, quantity, and location.  
- **Order Management**: Create, update, and track order history.  
- **User Management**: Maintain warehouse user accounts with roles and contact info.  
- **Scan Logging**: Log item scans for inward/outward movements and review history.  
- **API-driven**: Easy integration with other applications or front-end interfaces.  


## 🧩 Tech Stack

The Smart Warehouse Management System is built using the following technologies:

- **Framework:** [Frappe Framework](https://frappeframework.com/)  
- **Programming Language:** Python 3.12+  
- **Frontend:** JavaScript (for DocType scripts)  
- **Database:** MariaDB / MySQL  
- **APIs:** REST API endpoints (JSON-based)  
- **Package & Build Management:** Yarn, Node.js  
- **Version Control:** Git & GitHub  
- **Development Server:** Frappe Bench  

## 🛠️  Installation

Follow these steps to get the Smart Warehouse app running:
```bash
1. Clone the repo
cd ~/frappe-bench/apps
git clone https://github.com/Abhijith-creator/smartwarehouse.git
cd ..

2. Install the app on your site
bench --site <site_name> install-app smart_warehouse
bench --site <site_name> migrate
bench build
```

## Test APIs

Import **smart_warehouse/api/smart_warehouse_collection.json** in Postman or Thunder Client and try endpoints like create_item, get_item, update_item, etc.

## 📜 License

MIT License © 2025 Abhijith Anbalagan

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)  
[![Frappe](https://img.shields.io/badge/Frappe-v15-orange)](https://frappeframework.com/)  

