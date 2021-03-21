from sqlalchemy.orm import Session

from src import models, schemas

def create_goal(db: Session, goal: schemas.GoalCreate):
    new_goal = models.Goal(title=goal.title, description=goal.description, isActive = goal.isActive, userId=goal.userId)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

def get_goals(db: Session, user_id):
    return db.query(models.Goal).filter(models.Goal.userId == user_id).all()

