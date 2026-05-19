from typing import Dict
from uuid import UUID
from app.schemas import Task

TasksDB : Dict[UUID, Task] = {}