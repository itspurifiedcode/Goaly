from src.controller import attachment_controller
from fastapi import APIRouter,HTTPException, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from src.database import get_db as getDB
from sqlalchemy.orm.session import Session
import os
import uuid
  
id = uuid.uuid4()
router = APIRouter()


@router.post("/api/attachment",  tags=["Attachment"])
async def image( db: Session = Depends(getDB),image: UploadFile = File(...)):
    print(image.file)
    # print('../'+os.path.isdir(os.getcwd()+"images"),"*************")
    try:
        os.mkdir("images")
        print(os.getcwd())
    except Exception as e:
        print(e) 
    originalName = image.filename.replace(" ", "-")
    name = originalName.split(".")[0]
    extension = originalName.split(".")[-1]
    modifiedName = name+"-"+str(id)+"."+extension
    url = os.getcwd()+"/images/"+ modifiedName
    with open(url,'wb+') as f:
        f.write(image.file.read())
        f.close()
    res = attachment_controller.attachments(db, originalName=originalName,modifiedName=modifiedName, url=url)
    return res
    # return {"id": 1,
    #                 "original_name": originalName,
    #                 "given_name": givenName,
    #                 "attachement_url": url,
    #                 }