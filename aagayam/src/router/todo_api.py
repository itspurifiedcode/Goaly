from typing import Optional
from fastapi import APIRouter, HTTPException, File, UploadFile, Form
from src import models, schemas
from fastapi.params import Depends
from src.database import get_db as getDB
from sqlalchemy.orm.session import Session
from src.controller import todos_controller
import json
from .. utils import save_file_to_disk
from ..controller import auth_controller

router = APIRouter()

#Add Todo
# {
#    "task": "string",
#    "goalId": 0,
#    "isActive": true
#  }
@router.post("/api/todo",  tags=["todo"])
def add_todo(todo:str = Form(...), image: UploadFile = File(...), db: Session = Depends(getDB), current_user: schemas.User = Depends(auth_controller.get_current_user)):
    jsonified = json.loads(todo)
    savedImage = save_file_to_disk(image, path="attachments", save_as="temp")
    jsonified.update({'url':savedImage})
    new_todo = todos_controller.create_todo(db, todo=jsonified)
    return new_todo

@router.get("/api/todo/{goal_id}", tags=["todo"])
def get_todos(goal_id: int, db: Session = Depends(getDB), current_user: schemas.User = Depends(auth_controller.get_current_user)):
    todos= todos_controller.get_todos_by_goalID(db, goal_id=goal_id)
    if not todos:
        raise HTTPException(status_code=404, detail="Invalid ID")
    return todos
