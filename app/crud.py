from sqlalchemy.orm import Session
from models import Task
from schemas import PostTask, ResponseTask, EditTask
from datetime import date


def get_all_tasks(db: Session, title: str | None = None, description: str | None = None, done: bool | None = None,
                  creation_date_begin: date | None = None, creation_date_end: date | None = None,
                  due_date_begin: date | None = None, due_date_end: date | None = None):
    query = db.query(Task)
    if title is not None:
        query = query.filter(Task.title.like(f'%{title}%'))
    if description is not None:
        query = query.filter(Task.description.like(f'%{description}%'))
    if done is not None:
        query = query.filter(Task.done == done)
    if creation_date_begin is not None:
        query = query.filter(Task.creation_date >= creation_date_begin)
    if creation_date_end is not None:
        query = query.filter(Task.creation_date <= creation_date_end)
    if due_date_begin is not None:
        query = query.filter(Task.due_date >= due_date_begin)
    if due_date_end is not None:
        query = query.filter(Task.due_date <= due_date_end)
    return query.all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task: PostTask):

    last_id = db.query(Task).order_by(Task.id.desc()).first()
    new_id = last_id.id + 1
    db_task = Task(id=new_id, title=task.title, description=task.description, due_date=task.due_date)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(db_task)
    db.commit()
    return db_task


def update_task(db: Session, task_id: int, updated_task: EditTask):
    db_task = db.query(Task).filter(Task.id == task_id).first()



    for attr, value in updated_task.dict().items():
        if value is not None:
            setattr(db_task, attr, value)
    db.commit()
    db.refresh(db_task)
    return db_task
