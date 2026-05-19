from typing import List, Optional
from uuid import UUID
from app.database import TasksDB
from app.schemas import Task, TaskCreate, TaskUpdate


def create_task(data: TaskCreate) -> Task:
    task = Task.from_create(data)
    TasksDB[task.id] = task
    return task

def get_all_tasks(completed: Optional[bool] = None) -> List[Task]:
    tasks = list(TasksDB.values())
    if completed is not None:
        tasks = [task for task in tasks if task.completed == completed]
    return tasks

def get_task_by_id(task_id: UUID) -> Task:
    task = TasksDB.get(task_id)
    if not task:
        raise ValueError("Task not found")
    return task

def update_task(task_id:UUID,data:TaskUpdate)->Task:
    task = get_task_by_id(task_id)
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    TasksDB[task_id] = task
    return task

def complete_task(task_id: UUID) -> Task:
    task = get_task_by_id(task_id)
    task.completed = True
    TasksDB[task_id] = task
    return task

def delete_task(task_id: UUID) -> None:
    get_task_by_id(task_id)  
    del TasksDB[task_id]