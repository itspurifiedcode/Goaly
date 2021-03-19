from typing import List, Optional
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pydantic.main import BaseModel
from sqlalchemy.orm.session import Session
from src import models, schemas
from src.database import get_db as getDB
from src.controller import users_controller

router = APIRouter()
# Add user 
@router.post("/users/", response_model=schemas.User, tags=['User'])
def create_user(user: schemas.UserCreate, db: Session = Depends(getDB)):
    db_user = users_controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_2= users_controller.create_user(db=db, user=user)
    print(user_2.hashed_password)
    return user_2

#  Get users
@router.get("/users/", response_model=List[schemas.User], tags=['User'])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(getDB)):
    users = users_controller.get_users(db, skip=skip, limit=limit)
    return users

# Get user with id
@router.get("/users/{user_id}", response_model=schemas.User, tags=['User'])
def read_user(user_id: int, db: Session = Depends(getDB)):
    db_user = users_controller.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
