from typing import List, Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    task: str
    goalId: int
    isActive: bool = True
    
    class Config:
        orm_mode = True
    
class TodoCreate(TodoBase):
    pass   
class Todo(TodoBase):
    pass   
class TodoImageUpload(TodoBase):
    imgUrl:str 

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    userId: int
    isActive: bool = True
    tasks: List[Todo] = []
    class Config:
        orm_mode = True
    
class GoalCreate(GoalBase):
    pass   

class Goal(GoalBase):
    id: int

class UserBase(BaseModel):
    email: str
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: Optional[bool] = True
    goals: List[Goal] = []

    class Config:
        orm_mode = True
    


