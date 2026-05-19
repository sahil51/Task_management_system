from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(...,min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    priority: int = Field(..., ge=1, le=5)
    
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    priority: Optional[int] = Field(default=None, ge=1, le=5)
    
class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    priority: int
    completed: bool
    
class Task(TaskResponse):
    @classmethod
    def from_create(cls, data:TaskCreate):
        return cls(
            id = uuid4(),
            title = data.title,
            description = data.description,
            priority = data.priority,
            completed = False
        )