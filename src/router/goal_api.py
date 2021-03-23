from src.schemas import goal_schema
from typing import List
from fastapi import APIRouter,HTTPException
from src.schemas import GoalCreate, Goal
from fastapi.params import Depends
from src.database import get_db as getDB
from sqlalchemy.orm.session import Session
from src.controller import goals_controller

router = APIRouter()

#Add Goal
@router.post("/api/goal",  tags=["goal"])
def add_goal(goal:GoalCreate, db: Session = Depends(getDB)):
    new_goal = goals_controller.create_goal(db, goal=goal)
    return new_goal

@router.get("/goals/{user_id}", response_model=List[Goal], tags=['goal'])
def get_goals_by_user_id(user_id: int, db: Session = Depends(getDB)):
    db_goal = goals_controller.get_goals(db, user_id=user_id)
    print(db_goal)
    if not db_goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return db_goal
