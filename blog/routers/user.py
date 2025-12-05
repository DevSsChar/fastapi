from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from blog.hashing import Hash
from sqlalchemy.orm import Session
# from requests import Session
from .. import schemas, models, database

router = APIRouter()

@router.post('/user',response_model=schemas.ShowUser,tags=["Users"])
def create_user(request:schemas.User, db:Session=Depends(database.get_db)):
    # hash the password before storing it
    hashed_password = Hash.bcrypt(request.password)
    new_user=models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser,tags=["Users"])
def get_user(id, db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user
