from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Query, status
from app.schemas import Task, TaskCreate, TaskUpdate,TaskResponse
from app import services

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("",response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_new_task(payload: TaskCreate):
    return services.create_task(payload)

@router.get("",response_model=List[TaskResponse])
def get_tasks(completed: Optional[bool]=Query(default=None)):
    return services.get_all_tasks(completed)

@router.get("/{task_id}",response_model=TaskResponse)
def get_task(task_id: UUID):
    return services.get_task_by_id(task_id)

@router.put("/{task_id}",response_model=TaskResponse)
def update_task(task_id:UUID, payload: TaskUpdate):
    return services.update_task(task_id, payload)

@router.patch('/{task_id}/complete', response_model=TaskResponse)
def mark_task_complete(task_id:UUID):
    return services.complete_task(task_id)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID):
    services.delete_task(task_id)