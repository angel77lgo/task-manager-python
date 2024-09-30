from datetime import datetime
from enum import Enum

from typing_extensions import TypedDict, Optional


class TaskCreate(TypedDict):
    title: str
    email: str
    description: str
    due_date: Optional[datetime]

class EmailInfo(TypedDict):
    subject: str
    message: str

class MailAction(Enum):
    CREATE: str = 'create'
    UPDATE: str = 'update'