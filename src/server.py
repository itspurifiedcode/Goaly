from fastapi import FastAPI, HTTPException
from .router import goal_api,todo_api,user_api
from . import  models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(goal_api.router)
app.include_router(user_api.router)
app.include_router(todo_api.router)

def error_response():
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/")
def read_root():
    return {"Hello": "Merk"}
