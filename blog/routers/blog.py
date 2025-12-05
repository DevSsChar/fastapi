from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
# from requests import Session
from .. import schemas, models, database

router = APIRouter()

@router.get('/blog',response_model=List[schemas.ShowBlog],tags=["Blogs"])
def all(db:Session=Depends(database.get_db)):
    # return all blogs and query on Blog from models
    blogs=db.query(models.Blog).all()
    return blogs

@router.post('/blog',tags=["Blogs"])
# use schemas.Blog to define the request body
# db should be instance of Session and use Depends to get the db session    
def create(request: schemas.Blog, db:Session=Depends(database.get_db)):
    # add new blog to the database
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    # pass instance of new_blog to refresh to get the new data with id
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def destroy(id, db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update(id, request:schemas.Blog, db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'updated'

# @app.get('/blog',response_model=List[schemas.ShowBlog])
# def all(db:Session=Depends(get_db)):
#     # return all blogs and query on Blog from models
#     blogs=db.query(models.Blog).all()
#     return blogs

# import status and use 201 for created
@router.get('/blog/{id}', status_code=201, response_model=schemas.ShowBlog, tags=["Blogs"])
def show(id, db:Session=Depends(database.get_db)):
    # get the blog with the given id
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # raise HTTPException if blog not found with status code and detail
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog