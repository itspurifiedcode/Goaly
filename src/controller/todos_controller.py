from fastapi import UploadFile
from sqlalchemy.orm import Session
from src import models, schemas

def create_todo(db: Session, todo: schemas.TodoCreate):
    new_todo = models.Todo(task=todo['task'], goalId=todo['goalId'], isActive = todo['isActive'], url=todo['url'])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def get_todos_by_goalID(db: Session,goal_id: int):
    return db.query(models.Todo).filter(models.Todo.goalId == goal_id).all()
    

