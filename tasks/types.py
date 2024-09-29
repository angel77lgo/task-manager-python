from datetime import datetime

from typing_extensions import TypedDict, Optional


class TaskCreate(TypedDict):
    title: str
    email: str
    description: str
    due_date: Optional[datetime]