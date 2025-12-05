from typing import List, Optional
from pydantic import BaseModel

# create the pydantic schemas here
class Blog(BaseModel):
    title: str
    body: str
    class Config:
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]=[]
    class Config:
        from_attributes = True

# to create a response model by extending the Blog schema
class ShowBlog(Blog):
    # need this Config class to work with ORM models
    user: Optional[ShowUser] = None  # Changed from creator to user
    class Config:
        from_attributes = True

class Login(BaseModel):
    email: str
    password: str