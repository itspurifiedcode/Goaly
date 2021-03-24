from sqlalchemy.orm import Session

from src import models, schemas

def create_todo(db: Session, todo: schemas.TodoCreate):
    new_todo = models.Todo(task=todo.task, goalId=todo.goalId, isActive = todo.isActive, url=todo.imgUrl)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

