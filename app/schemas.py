from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class BaseTask(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: Optional[str]
    due_date: Optional[datetime]


class PostTask(BaseTask):
    pass


class ResponseTask(BaseTask):
    id: int
    creation_date: datetime
    status: bool


class EditTask(BaseTask):
    title: Optional[str]
    status: Optional[bool]
