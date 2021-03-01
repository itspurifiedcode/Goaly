from src.router import user_api
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .router import goal_api
from . import  models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(goal_api.router)
app.include_router(user_api.router)

def error_response():
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/")
def read_root():
    return {"Hello": "World"}
