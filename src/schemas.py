from typing import List, Optional

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
    
