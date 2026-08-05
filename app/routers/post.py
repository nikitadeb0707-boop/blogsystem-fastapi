from fastapi import FastAPI, Body,Response,status,HTTPException, Depends,APIRouter
from pydantic import BaseModel
from typing import Optional
import psycopg2,time
from psycopg2.extras import RealDictCursor
import models,schemas, utilts
from database import engine, getdb
from random import randrange
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from utilts import hash_password
import oauth2
import sys
from typing import List
from sqlalchemy import func
#@app.get("/sqlalchemy")
#def test(db:Session = Depends(getdb)):
#  posts =   db.query(models.Post).all()
 # return{"status":posts}
router= APIRouter(
     prefix="/posts",
     tags=['posts']
)     
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.Response)
def createpost(post: schemas.CreatePost, db:Session = Depends(getdb),currentuser:int=Depends(oauth2.getcurrentuser)):
    #cursor.execute(""" INSERT INTO posts(title,content,published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
    #newpost=cursor.fetchone()
    #conn.commit()
   ## newpost = models.Post(title= post.title,content=post.content, published=post.published)
    newpost = models.Post(ownerid=currentuser.id, **post.dict())
    db.add(newpost)
    db.commit()
    db.refresh(newpost)
    return newpost



        
@router.get("/")
def getposts(db:Session= Depends(getdb),limit:int=5,skip:int=0, search:Optional[str]=""):
    #cursor.execute("""SELECT * FROM posts""")
     #posts=cursor.fetchall()
     posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
     results=db.query(models.Post,func.count(models.Vote.postid.label("votecount"))).join(models.Vote,models.Vote.postid==models.Post.id,isouter=True).filter(models.Post.title.contains(search)).group_by(models.Post.id).limit(limit).offset(skip).all()

     print(posts)
     return [{"votecount": vc, **post.__dict__} for post, vc in results]

@router.get("/{id}", response_model=schemas.Response)
def getpost(id: int , response : Response, db:Session=Depends(getdb)):
   #cursor.execute("""SELECT * FROM posts WHERE id = %s""", str((id)))
   #post= cursor.fetchone()
   post = db.query(models.Post).filter(models.Post.id==id).first()
   #use .all() to search if id was a repeatable column
   print (post)
   if not post:
           response.status_code = 404
           return {"message": "post not found"}
   return post

@router.delete("/{id}" , status_code= status.HTTP_204_NO_CONTENT)
def delete(id:int,db:Session=Depends(getdb),currentuser:int=Depends(oauth2.getcurrentuser)):
    #cursor.execute("""DELETE FROM posts WHERE id=%s returning *""",str((id)))
    #post=cursor.fetchone()
    #conn.commit()
    qpost=db.query(models.Post).filter(models.Post.id==id)
    post=qpost.first()
    if post==None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    if post.ownerid!=currentuser.id:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)    
    qpost.delete(synchronize_session=False)
    db.commit()
    return post
@router.put("/{id}",response_model=schemas.Response)
def updatepost(id:int,updatedpost:schemas.Post,db:Session=Depends(getdb),currentuser:int=Depends(oauth2.getcurrentuser)):
      #cursor.execute("""UPDATE posts SET title=%s,content=%s,published=%s WHERE id=%s RETURNING *""", (post.title,post.content,post.published, str(id)))                                                                                                 
      #updatedpost=cursor.fetchone()
      #conn.commit()
      qpost= db.query(models.Post).filter(models.Post.id==id)
      post=qpost.first()
     
      if post == None:
          raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
      if post.ownerid!=currentuser.id:
           raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
      qpost.update(updatedpost.dict(),synchronize_session= False)
      db.commit()
      return qpost.first()