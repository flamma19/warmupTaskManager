from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, date


class BaseTask(BaseModel):
    title: str
    description: str | None = None
    due_date: date | None = None

    class Config:
        from_attributes = True
class PostTask(BaseTask):
    pass


class ResponseTask(BaseTask):
    id: int
    creation_date: date
    done: bool


class EditTask(BaseTask):
    title: Optional[str]
    done: Optional[bool]
