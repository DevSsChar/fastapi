from typing import List
# import depends for dependency injection
# import status for displaying status codes and HTTPException for raising exceptions
from fastapi import FastAPI, Depends, status, HTTPException
# import session from orm
from sqlalchemy.orm import Session
# import the schemas module
from . import schemas,models
# import engine and session(variable) from the db module
from .database import engine,get_db
# import passlib to hash passwords
# from passlib.context import CryptContext
# import the Hash class from hashing module
from .hashing import Hash
from .routers import blog,user,authentication

app = FastAPI()

# make the engine work and create the database tables
models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

