from pydantic import BaseModel

# create the pydantic schemas here
class Blog(BaseModel):
    title: str
    body: str