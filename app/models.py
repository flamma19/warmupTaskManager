from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Task(Base):
    __tablename__: str = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    creation_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    due_date: Mapped[DateTime] = mapped_column(DateTime)

