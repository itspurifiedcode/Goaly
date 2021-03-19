from typing import Optional
from fastapi import APIRouter
from pydantic.main import BaseModel
from src import models, schemas
from fastapi.params import Depends
from src.helper import get_db as getDB
from sqlalchemy.orm.session import Session
from src.controller import todos_controller

router = APIRouter()

class Todo(BaseModel):
    title: str
    status: Optional[int ] = 1
    description: str
    isActive : Optional[bool] = True

#Add Todo
@router.post("/api/todo",  tags=["todo"])
def add_todo(todo:schemas.TodoBase, db: Session = Depends(getDB)):
    new_todo = goals_controller.create_goal(db, todo=todo)
    return new_todo

@router.get("/api/todo", tags=["todo"])
def get_todos():
    return {"todo":[]}
