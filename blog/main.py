# import depends for dependency injection
from fastapi import FastAPI, Depends
# import session from orm
from sqlalchemy.orm import Session
# import the schemas module
from . import schemas,models
# import engine and session(variable) from the db module
from .database import engine,SessionLocal

app = FastAPI()

# make the engine work and create the database tables
models.Base.metadata.create_all(bind=engine)

# write get_db function to get the db session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
# use schemas.Blog to define the request body
def create(request: schemas.Blog, db:Session=Depends(get_db)):
    # add new blog to the database
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    # pass instance of new_blog to refresh to get the new data with id
    db.refresh(new_blog)
    return new_blog

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8001)