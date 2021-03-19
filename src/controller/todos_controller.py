from sqlalchemy.orm import Session

from src import models, schemas

def create_todo(db: Session, goal: schemas.TodoCreate):
    new_todo = models.Goal(title=todo.task, goalId=todo.goalId, isActive = todo.isActive)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
