from fastapi import FastAPI, HTTPException, File, UploadFile
from .router import goal_api,todo_api,user_api
from . import  models
from .database import engine
from .utils import save_file_to_disk


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


@app.post("/uploadimage/")
def upload_image(image: UploadFile = File(...)):
    return  save_file_to_disk(image, path="attachments", save_as="temp")

