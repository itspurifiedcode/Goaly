from src.utils import Hash
from src import utils
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm.session import Session
from src import models
from src.schemas import auth_schema
from src.database import get_db as getDB
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Auth'])

@router.post("/login")
def user_login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(getDB)):
    dbUser = db.query(models.User).filter(models.User.email == user.username).first()
    if dbUser:
        checkPassword = Hash.verify_password(user.password, dbUser.hashedPassword)
        if checkPassword:
            access_token = utils.create_access_token(data={"email": dbUser.email, "id":dbUser.id})
            return {"access_token": access_token, "token_type": "bearer"}

        else:
            raise HTTPException(status_code=400, detail="Invalid Credentials")
    else:
        raise HTTPException(status_code=400, detail="Email not found")
    