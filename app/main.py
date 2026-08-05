from fastapi import FastAPI, Body,Response,status,HTTPException, Depends, APIRouter
#import psycopg2,time
from psycopg2.extras import RealDictCursor
import models,schemas, utilts
from database import engine, getdb
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from utilts import hash_password
from routers import post,user,auth,vote
from config import Settings
##models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
      
    
    
    