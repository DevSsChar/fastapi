from typing import List
from pydantic import BaseModel

# create the pydantic schemas here
class Blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode=True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]=[]
    class Config:
        orm_mode=True

# to create a response model by extending the Blog schema
class ShowBlog(Blog):
    # need this Config class to work with ORM models
    # removed in newer versions of pydantic
    creator: ShowUser
    class Config:
        orm_mode=True