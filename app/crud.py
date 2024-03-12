from sqlalchemy.orm import session
from models import Task
from schemas import PostTask, ResponseTask, EditTask

def get_all_tasks(db: session ):
    return db.query(Task).all()

def get_task_by_id(db: session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: session, task: PostTask):
    db_task = Task(title=task.title, description=task.description, due_date=task.due_date)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(db_task)
    db.commit()

def update_task(db: session, task_id: int, task: EditTask):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db_task.title = task.title
    db_task.description = task.description
    db_task.due_date = task.due_date
    db_task.status = task.status
    db.commit()
    db.refresh(db_task)
    return db_task
