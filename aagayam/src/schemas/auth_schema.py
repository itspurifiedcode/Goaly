from typing import List, Optional

from .goal_schema import Goal
from pydantic import BaseModel

class AuthBase(BaseModel):
    email: str
    password: str
    class Config:
        orm_mode = True
    

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: Optional[str] = None
    id: Optional[str] = None
