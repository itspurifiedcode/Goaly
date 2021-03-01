from typing import Optional
from fastapi import APIRouter
from pydantic.main import BaseModel

router = APIRouter()

class Goal(BaseModel):
    title: str
    status: Optional[int ] = 1
    description: str
    isActive : Optional[bool] = True


@router.post("/api/goal", tags=["goal"])
def add_goal(goal:Goal):
    return goal

@router.get("/api/goals", tags=["goal"])
def get_goals():
    return {"goals":[]}
