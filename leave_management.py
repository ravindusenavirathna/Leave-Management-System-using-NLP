from datetime import datetime, timedelta
from typing import List
from models import LeaveRequest
from ai_handler import GeminiAIHandler


class LeaveManagementSystem:
    def __init__(self, ai_handler: GeminiAIHandler):
        self.ai_handler = ai_handler
        self.employees = {
            "alice": {"sick_leave": 5, "annual_leave": 10, "maternity_leave": 0},
            "bob": {"sick_leave": 8, "annual_leave": 15, "maternity_leave": 0},
            "charlie": {"sick_leave": 2, "annual_leave": 12, "maternity_leave": 0}
        }
        self.leave_history: List[LeaveRequest] = []

    async def process_query(self, employee: str, query: str) -> str:
        """Process user query using Gemini AI and execute appropriate action"""
        if employee not in self.employees:
            return f"Employee {employee} not found."

        analysis = await self.ai_handler.analyze_query(query)
        handlers = {
            "check_balance": self._handle_balance_query,
            "request_leave": self._handle_leave_request,
            "cancel_leave": self._handle_leave_cancellation,
            "view_history": self._handle_history_query
        }

        handler = handlers.get(analysis["intent"])
        if handler:
            return await handler(employee, analysis)

        return "I couldn't understand your request. Please try rephrasing."

    async def _handle_balance_query(self, employee: str, analysis: dict) -> str:
        """Handle balance check requests"""
        if analysis["leave_type"]:
            balance = self.employees[employee][analysis["leave_type"]]
            return f"You have {balance} {analysis['leave_type'].replace('_', ' ')}(s) remaining."

        balances = [
            f"{k.replace('_', ' ')}: {v}"
            for k, v in self.employees[employee].items()
        ]
        return "Your leave balances:\n" + "\n".join(balances)

    async def _handle_leave_request(self, employee: str, analysis: dict) -> str:
        """Handle leave requests"""
        if not all([analysis["leave_type"], analysis["days"], analysis["start_date"]]):
            return "Please provide leave type, number of days, and start date."

        start_date = datetime.strptime(analysis["start_date"], "%Y-%m-%d")
        days_requested = int(analysis["days"])
        current_balance = self.employees[employee][analysis["leave_type"]]

        if days_requested > current_balance:
            return f"Insufficient leave balance. You have {current_balance} {analysis['leave_type']} left."

        end_date = start_date + timedelta(days=days_requested - 1)
        leave_request = LeaveRequest(
            employee=employee,
            leave_type=analysis["leave_type"],
            start_date=start_date,
            end_date=end_date,
            status="approved",
            days_requested=days_requested
        )

        self.employees[employee][analysis["leave_type"]] -= days_requested
        self.leave_history.append(leave_request)

        return f"Leave approved: {analysis['leave_type']} from {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}."

    async def _handle_leave_cancellation(self, employee: str, analysis: dict) -> str:
        """Handle leave cancellation requests"""
        if not analysis["start_date"]:
            return "Please specify the date of the leave you want to cancel."

        cancel_date = datetime.strptime(analysis["start_date"], "%Y-%m-%d")

        for request in self.leave_history:
            if (request.employee == employee and request.status == "approved" and
                    request.start_date <= cancel_date <= request.end_date):

                self.employees[employee][request.leave_type] += request.days_requested
                request.status = "cancelled"

                return f"Successfully cancelled {request.days_requested} day(s) of {request.leave_type} starting from {request.start_date.strftime('%B %d, %Y')}."

        return "No matching leave request found for the specified date."

    async def _handle_history_query(self, employee: str, analysis: dict) -> str:
        """Handle leave history queries"""
        employee_history = [
            req for req in self.leave_history if req.employee == employee]

        if not employee_history:
            return "No leave history found."

        return "\n".join([
            f"{req.leave_type} - {req.days_requested} day(s), {req.start_date.strftime('%B %d, %Y')} to {req.end_date.strftime('%B %d, %Y')}, Status: {req.status}"
            for req in employee_history
        ])
