from fastapi import FastAPI, Body,Response,status,HTTPException, Depends,APIRouter
import schemas, database, oauth2,models
from sqlalchemy.orm import Session
router= APIRouter(
    prefix="/vote",
    tags=['vote']
)
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session=Depends(database.getdb),currentuser:int=Depends(oauth2.getcurrentuser)):
    post= db.query(models.Post).filter(models.Post.id==vote.postid).first()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"post doesnt exist")
    votequery=db.query(models.Vote).filter(models.Vote.postid==vote.postid,models.Vote.userid==currentuser.id)
    votefound=votequery.first()
    if (vote.dir==1):
       if votefound:
           raise HTTPException(status.HTTP_409_CONFLICT, detail=f"user has already voted")
       newvote=models.Vote(postid=vote.postid,userid=currentuser.id)
       db.add(newvote)
       db.commit()
       return{"detail":f"like updated on {vote.postid}"}
    else:
        if not votefound:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="vote does not exist"
        )
        votequery.delete(synchronize_session=False)
        db.commit()
        return{"detail":"like deleted"}
