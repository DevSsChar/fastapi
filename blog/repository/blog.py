from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import models, database, schemas
from typing import List

def all(db:Session):
    # return all blogs and query on Blog from models
    blogs=db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db:Session=Depends(database.get_db)):
    # add new blog to the database
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    # pass instance of new_blog to refresh to get the new data with id
    db.refresh(new_blog)
    return new_blog

def destroy(id, db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

def update(id, request:schemas.Blog, db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'updated'

def show(id, db:Session=Depends(database.get_db)):
    # get the blog with the given id
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # raise HTTPException if blog not found with status code and detail
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog