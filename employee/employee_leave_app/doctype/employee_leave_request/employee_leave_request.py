# Copyright (c) 2026, chakri and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
from frappe.utils import date_diff

class EmployeeLeaveRequest(Document):

    def validate(self):
        self.validate_dates()
        self.calculate_total_days()
        self.check_approval_rules()

    def validate_dates(self):
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                frappe.throw("From Date must be earlier than or equal to To Date")

    def calculate_total_days(self):
        if self.from_date and self.to_date:
            self.total_days = date_diff(self.to_date, self.from_date) + 1

    def check_approval_rules(self):
        if self.status == "Approved":

        
            if "HR Manager" not in frappe.get_roles():
                frappe.throw("Only HR can approve leave requests")

    
            employee_user = frappe.db.get_value(
                "Employee", self.employee, "user_id"
            )

            if employee_user == frappe.session.user:
                frappe.throw("You cannot approve your own leave request")

