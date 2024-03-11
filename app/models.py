from sqlalchemy import Integer, String, DateTime, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__: str = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(Enum('not done', 'doing', 'done'), nullable=False, default='not done')
    creation_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    due_date: Mapped[DateTime] = mapped_column(DateTime)

