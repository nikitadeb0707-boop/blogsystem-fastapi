from fastapi import FastAPI, Body,Response,status,HTTPException, Depends,APIRouter
import models,schemas, utilts
from database import  getdb
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from utilts import hash_password
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
router= APIRouter(
     tags= ['users']
)
@router.post("/users",status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)  
def createuser( user:schemas.CreateUser,db:Session = Depends(getdb)): 
     #hash the password user.password
     hpassword = utilts.hash_password(user.password)
     user.password = hpassword
     new_user= models.User(**user.dict())
     try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
     except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
     return new_user
@router.get("/users/{id}", response_model=schemas.UserOut)
def getpost(id: int , response : Response, db:Session=Depends(getdb)):
   user = db.query(models.User).filter(models.User.id==id).first()
   #use .all() to search if id was a repeatable column
   
   if not user:
           response.status_code = 404
           return {"message": "user not found"}
   return user
 