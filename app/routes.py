from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Body, Request
from db import get_db
from sqlalchemy.orm import Session
from schemas import ResponseTask, PostTask, EditTask
import crud

router = APIRouter(
    prefix='/tasks',
)


@router.get('/', response_model=List[ResponseTask])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_all_tasks(db)
    if tasks:
        return tasks
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No tasks found')


@router.get('/{task_id}', response_model=ResponseTask)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with id {task_id} not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return task


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ResponseTask)
async def create_task(task: PostTask, db: Session = Depends(get_db)):
    new_task = crud.create_task(db, task)
    return new_task


@router.delete('/{task_id}', response_model=ResponseTask)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id=task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with id {task_id} not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    deleted_task = crud.delete_task(db, task_id)
    return deleted_task


@router.put('/{task_id}', response_model=ResponseTask)
async def update_task(task_id: int, updated_task: EditTask, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id=task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with id {task_id} not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    edited_task = crud.update_task(db, task_id=task_id, updated_task=updated_task)
    return edited_task

