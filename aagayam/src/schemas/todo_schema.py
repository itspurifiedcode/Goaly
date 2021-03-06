from typing import List, Optional
from pydantic import BaseModel   

class TodoBase(BaseModel):
    task: str
    goalId: int
    isActive: bool = True
    url: str
    
    class Config:
        orm_mode = True
    
class TodoCreate(TodoBase):
    pass  

class Todo(TodoBase):
    id : int
