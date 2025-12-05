from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
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
# oauth2passwordrequestform is used to get the username and password from the request form
# else we would get a 422 error that unprocessable entity
def login(OAuth2PasswordRequestForm: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==OAuth2PasswordRequestForm.username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND
                             ,detail="Invalid Credentials")
    if not Hash.verify(user.password,OAuth2PasswordRequestForm.password):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND
                             ,detail="Invalid Credentials")
    # access_token_expires = timedelta(minutes=access_token_expire_minutes) optional
    access_token = create_access_token(
        data={"sub": user.email}
        #, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}