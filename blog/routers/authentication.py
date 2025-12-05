from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas,database,models
from ..hashing import Hash
from sqlalchemy.orm import Session
from datetime import timedelta
from ..JWTtoken import create_access_token, access_token_expire_minutes
router = APIRouter(
    tags=["Authentication"],
)

@router.post('/login',status_code=status.HTTP_200_OK)
# get_db is not callable here, so we use Depends to get the db session
def login(request:schemas.Login,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.email).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND
                             ,detail="Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND
                             ,detail="Invalid Credentials")
    # access_token_expires = timedelta(minutes=access_token_expire_minutes) optional
    access_token = create_access_token(
        data={"sub": user.email}
        #, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}