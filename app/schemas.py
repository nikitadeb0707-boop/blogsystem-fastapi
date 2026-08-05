from pydantic import BaseModel, EmailStr,conint
from datetime import datetime
from typing import Optional,Literal
class UserOut(BaseModel):
     id:int
     email:EmailStr
     created_at: datetime
     class Config:
        from_attributes = True

class Post(BaseModel):
    
    title: str
    content: str  
    published: bool = True
class CreatePost(Post):
    pass
class UpdatePost(Post):
     pass
class Response(BaseModel):
     id:int
     title: str
     content: str
     published: bool = True
     createdat: datetime
     owner: UserOut
     class Config:
          from_attributes = True
class CreateUser(BaseModel):
     email:EmailStr
     password:str


class Token(BaseModel):
     accesstoken:str
     tokentype:str

class TokenData(BaseModel):
     id:Optional[int]=None  
class Vote(BaseModel):
     postid:int
     #dir:conint(ge=0,le=1)
     dir:Literal[0,1]