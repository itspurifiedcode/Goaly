from src import schemas, controller
from typing import List
from fastapi import APIRouter,HTTPException, File, UploadFile, Form
from src.schemas import GoalCreate, Goal
from fastapi.params import Depends
from src.database import get_db as getDB
from sqlalchemy.orm.session import Session
from src.controller import auth_controller, goals_controller, attachment_controller
import json
from .. utils import save_file_to_disk
import uuid

router = APIRouter()

#Add Goal
@router.post("/api/goal",  tags=["goal"])
def add_goal(goal:GoalCreate, db: Session = Depends(getDB), current_user: schemas.User = Depends(auth_controller.get_current_user)):
    new_goal = goals_controller.create_goal(db, goal=goal)
    return new_goal

@router.get("/goals/{user_id}", response_model=List[Goal], tags=['goal'])
def get_goals_by_user_id(user_id: int, db: Session = Depends(getDB), current_user: schemas.User = Depends(auth_controller.get_current_user)):
    db_goal = goals_controller.get_goals(db, user_id=user_id)
    if not db_goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return db_goal

@router.get("/goal/{goal_id}", tags=['goal'])
def get_goals_by_goal_id(goal_id: int, db: Session = Depends(getDB), current_user: schemas.User = Depends(auth_controller.get_current_user)):
    print(goal_id)
    print(current_user)
    db_goal = goals_controller.get_goal_by_id(db, user_id=current_user.id, goal_id=goal_id)
    attIDs = db_goal.attachmentIDs
    attachments = attachment_controller.get_attachments_by_ids(db, attIDs)
    db_goal.attachments = attachments
    del db_goal.attachmentIDs
    if not db_goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return db_goal