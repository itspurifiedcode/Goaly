from typing import List, Optional
from pydantic import BaseModel
from .goal_schema import Goal

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