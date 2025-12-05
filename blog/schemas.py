from pydantic import BaseModel

# create the pydantic schemas here
class Blog(BaseModel):
    title: str
    body: str

# to create a response model by extending the Blog schema
class ShowBlog(Blog):
    # need this Config class to work with ORM models
    # removed in newer versions of pydantic
    class Config:
        orm_mode=True

class User(BaseModel):
    name: str
    email: str
    password: str