from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass
class LeaveRequest:
    employee: str
    leave_type: str
    start_date: datetime
    end_date: datetime
    status: str
    days_requested: int


class IntentType(Enum):
    CHECK_BALANCE = "check_balance"
    REQUEST_LEAVE = "request_leave"
    CANCEL_LEAVE = "cancel_leave"
    VIEW_HISTORY = "view_history"
    UNKNOWN = "unknown"
