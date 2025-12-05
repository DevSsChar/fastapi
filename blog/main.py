from typing import List
# import depends for dependency injection
# import status for displaying status codes and HTTPException for raising exceptions
from fastapi import FastAPI, Depends, status, HTTPException
# import session from orm
from sqlalchemy.orm import Session
# import the schemas module
from . import schemas,models
# import engine and session(variable) from the db module
from .database import engine,SessionLocal
# import passlib to hash passwords
# from passlib.context import CryptContext
# import the Hash class from hashing module
from .hashing import Hash

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
# db should be instance of Session and use Depends to get the db session    
def create(request: schemas.Blog, db:Session=Depends(get_db)):
    # add new blog to the database
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    # pass instance of new_blog to refresh to get the new data with id
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'updated'

@app.get('/blog',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db)):
    # return all blogs and query on Blog from models
    blogs=db.query(models.Blog).all()
    return blogs

# import status and use 201 for created
@app.get('/blog/{id}', status_code=201, response_model=schemas.ShowBlog)
def show(id, db:Session=Depends(get_db)):
    # get the blog with the given id
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # raise HTTPException if blog not found with status code and detail
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog

# we use argon2 here since bcrypt was cracking
# pwd_cxt=CryptContext(schemes=["argon2"], deprecated="auto")

@app.post('/user',response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):
    # hash the password before storing it
    hashed_password = Hash.bcrypt(request.password)
    new_user=models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8001)