from sqlalchemy import Integer, String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Task(Base):
    __tablename__: str = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    creation_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())
    due_date: Mapped[date] = mapped_column(Date, nullable=True)

