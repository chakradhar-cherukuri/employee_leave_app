
# About the App

**Employee Leave App** is a custom Frappe application that extends HR functionality by managing employee leave processes in a simple and structured way.

The app is designed to work **alongside HRMS** and uses the existing **Employee doctype** provided by the HRMS app. It does **not duplicate core HR doctypes**.

---

## What This App Does (How It Works)

- Uses existing **Employee** records from HRMS
- Allows employees to raise new leave requests
- Automatically calculates total leave days based on selected dates
- Enforces validation rules before submission
- Routes leave requests **only for HR approval**
- Provides **list and history views** of employee leave requests

---

## Typical Flow

1. Employee logs in
2. Employee creates a new **Leave Request**
3. System validates dates and calculates total leave days
4. Leave request is submitted for approval
5. HR reviews and approves/rejects the request
6. Employee tracks request status in list view

---

## Roles and Permissions

### Employee Role
- Can create new leave requests
- Can view their own leave requests in **List View**

### HR Role
- Can review employee leave requests
- Can approve or reject leave requests
-  Cannot approve/reject their own leave request

---

## Prerequisites

Before installing this app, ensure the following are installed:

- Ubuntu / Linux
- Python **3.10+**
- Node.js **18+**
- Yarn
- Redis
- MariaDB / MySQL
- Frappe Bench
- **HRMS App (Mandatory)**

---

## Installation

### Step 1: Get Employee Leave App from GitHub

```bash
cd frappe-bench
bench get-app https://github.com/chakradhar-cherukuri/employee_leave_app.git
bench --site site_name install-app employee_leave_app


