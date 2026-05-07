from fastapi import FastAPI, Body,Response,status
from pydantic import BaseModel
from typing import Optional

from random import randrange

app = FastAPI()
myposts = []



class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
   
def findpost(id):
    for p in myposts:
        if p['id'] == id:
            return p
        
@app.post("/posts")
def createpost(post: Post):
    postdict = post.dict()
    postdict['id'] = randrange(0, 10)
    myposts.append(postdict)
    return {"data": postdict}



def findpost2(id):
    for i,p in enumerate(myposts):
        if p['id'] == id:
          return i

@app.get("/posts/{id}")
def getpost(id: int , response : Response):
    post= findpost(id)
    print (post)
    if not post:
        response.status_code = 404
        return {"message": "post not found"}
    return{"postdetail":post}

@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete(id:int):
    index = findpost2(id)
    myposts.pop(index)
   
    return{"message":"post deleted"}