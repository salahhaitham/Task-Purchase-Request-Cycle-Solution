# Purchase Request Task – Odoo 18

## Overview
This module extends the Purchase application in Odoo by introducing a Purchase Request workflow.  
Users can create purchase requests, add multiple request lines, and generate RFQs automatically after approval.

The module is designed to simulate a real business approval cycle before creating Purchase Orders.

---

# Features

## Purchase Request Management
- Create Purchase Requests
- Add multiple request lines
- Track request state:
  - Draft
  - Confirmed

---

## Purchase Request Fields
The Purchase Request form includes:

- Request Reference
- State
- Analytic Account
- Creation Date (readonly)
- Created By (readonly)
- Requested By
- Requested On
- Purchase Request Lines

---

## Purchase Request Lines
Each request line contains:

- Product
- Vendor
- Quantity
- Unit of Measure

---

# Automatic RFQ Generation

When the Purchase Request is confirmed:

- The system loops through all request lines
- Lines are grouped by Vendor
- A separate RFQ (draft Purchase Order) is automatically created for each vendor
- Purchase Order Lines are generated automatically

Example:

| Vendor | Products |
|---|---|
| Dell | Laptop, Keyboard |
| HP | Mouse |

Result:
- RFQ 1 → Dell
- RFQ 2 → HP

---

# Smart Buttons

## In Purchase Request
A smart button displays:
- All generated Purchase Orders

## In Purchase Order
A smart button displays:
- The related Purchase Request

---

# Security & Behavior

## Readonly After Confirmation
Once the Purchase Request is confirmed:
- All fields become readonly
- Request lines become readonly

This prevents modifying approved requests.

---

# Technical Concepts Used

This module demonstrates several important Odoo backend concepts:

- ORM Models
- One2many / Many2one Relations
- Business Logic Automation
- State Management
- Smart Buttons
- Domains
- Record Grouping
- Purchase Integration
- Action Methods
- Computed Counts

---

# Module Structure

```bash
purchase_request/
│
├── models/
│   ├── purchase_request.py
│   ├── purchase_request_line.py
│   └── purchase_order.py
│
├── views/
│   ├── purchase_request_views.xml
│   ├── purchase_order_views.xml
│   └── menus.xml
│
├── security/
│   ├── ir.model.access.csv
│
├── __init__.py
├── __manifest__.py
