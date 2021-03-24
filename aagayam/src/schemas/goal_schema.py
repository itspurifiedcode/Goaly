from typing import List, Optional
from .todo_schema import Todo
from pydantic import BaseModel

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    userId: int
    isActive: bool = True
    
    class Config:
        orm_mode = True
    
class GoalCreate(GoalBase):
    pass   

class Goal(GoalBase):
    id: int
    tasks: List[Todo] = []

# class GoalWithTodo(Goal):
    
