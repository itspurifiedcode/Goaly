from typing import Optional
from fastapi import APIRouter
from pydantic.main import BaseModel
from src import models, schemas
from fastapi.params import Depends
from src.database import get_db as getDB
from sqlalchemy.orm.session import Session
from src.controller import todos_controller

router = APIRouter()


#Add Todo
@router.post("/api/todo",  tags=["todo"])
def add_todo(todo:schemas.TodoBase, db: Session = Depends(getDB)):
    new_todo = todos_controller.create_todo(db, todo=todo)
    return new_todo

@router.get("/api/todo", tags=["todo"])
def get_todos():
    return {"todo":[]}
