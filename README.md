
>>>About the App

Employee Leave App is a custom Frappe that extends the HR functionality by managing employee leave processes in a simple and structured way.

The app is designed to work alongside HRMS and uses the Employee doctype provided by the HRMS app. It does not duplicate core HR doctypes.

>>> What This App Does (How It Works)

Uses existing Employee records from HRMS

Allows employees to raise new leave requests

Automatically calculates total leave days based on selected dates

Enforces validation rules before submission

Routes leave requests for HR approval only

Provides list and history view of employee leave requests

>>Typical flow:

Employee logs in

Employee creates a new Leave Request

System validates dates and calculates total days

Leave request is submitted for approval

HR reviews and approves/rejects the request

Employee can track status in list view

>>>Prerequisites

Before using this app, ensure the following are installed:

Ubuntu / Linux

Python 3.10 or later

Node.js 18+

Yarn

Redis

MariaDB / MySQL

Frappe Bench

HRMS app (mandatory)

>>>
Step 1: 
Get Employee Leave App (From GitHub)

Install from GitHub
cd frappe-bench
bench get-app https://github.com/chakradhar-cherukuri/employee_leave_app.git
bench --site site_name install-app employee

Step 2: Migrate and Restart
bench migrate
bench restart

Step 3: Using the App

Login to ERPNext

Open the Employee Leave App module

Select an Employee

Create or manage leave-related records provided by this app

View lists and reports

All Employee data comes from HRMS to Employee

>>>Common Commands 
Git Workflow 
git pull 
git status
git add .
git commit -m "Meaningful message"
git push

>>>App Structure Overview
employee_leave_app/
├── employee_leave_app/
│   ├── doctype/
│   ├── report/
│   ├── hooks.py
│   └── api.py
├── README.md
├── setup.py
└── pyproject.toml


