from fastapi import APIRouter, Depends, HTTPException, status
from db import get_db
from sqlalchemy.orm import Session
from schemas import ResponseTask, PostTask, EditTask
import crud

router = APIRouter(
    prefix='/tasks',
)


@router.get('/', response_model=list[ResponseTask])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_all_tasks(db)
    return {'code': 'success', 'status': status.HTTP_200_OK, 'response': tasks}


@router.get('/{task_id}', response_model=ResponseTask)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with id {task_id} not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return {'code': 'success', 'status': status.HTTP_200_OK, 'response': task}


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ResponseTask)
async def create_task(task: PostTask, db: Session = Depends(get_db)):
    new_task = crud.create_task(db, task)
    return {'code':'success','status': status.HTTP_201_CREATED,'response': new_task}


@router.delete('/{task_id}', response_model=ResponseTask)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id=task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with id {task_id} not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    crud.delete_task(db, task_id)
    return {'code': 'success', 'status': status.HTTP_200_OK, 'response': task}


@router.put('/{task_id}', response_model=ResponseTask)
async def update_task(task_id: int, task: EditTask, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id=task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with id {task_id} not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    crud.update_task(db, task_id=task_id, task=task)
    return {'code': 'success', 'status': status.HTTP_200_OK, 'response': task}

