from src.router import attachment_api
from typing import List, Optional
from .todo_schema import Todo
from pydantic import BaseModel

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    isActive: bool = True
    attachmentIDs : List = []

    class Config:
        orm_mode = True
    
class GoalCreate(GoalBase):
    userId: int   

class Goal(GoalBase):
    id: int
    tasks: List[Todo] = []

