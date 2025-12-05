from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import JWTtoken

# in tokenurl give the router path where the login endpoint is created
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(data: Annotated[str, Depends(oauth2_scheme)]):
    # create an exception for invalid credentials   
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}, 
    )

    return JWTtoken.verify_access_token(data, credentials_exception)

    