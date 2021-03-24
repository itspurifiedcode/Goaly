from typing import List, Optional
from .goal_schema import Goal
from pydantic import BaseModel

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