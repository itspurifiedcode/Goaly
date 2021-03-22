from typing import List, Optional
from pydantic import BaseModel
from .todo_schema import Todo

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    userId: str
    isActive: bool = True
    tasks: List[Todo] = []
    class Config:
        orm_mode = True
    
class GoalCreate(GoalBase):
    pass   

class Goal(GoalBase):
    id: int
