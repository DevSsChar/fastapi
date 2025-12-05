from fastapi import FastAPI
from typing import Optional
# create an instance of the app using FASTAPI
app=FastAPI()

# give path operation decorator, to create a route
@app.get('/')
def index():
    return {'data':{'name':'dev'}}

@app.get('/about')
def about():
    return {'data':'about page'}

# query parameters are defined in the function parameters and not given in path
# also to define their type, we can use type hints :int, :str, :bool, etc
# Optional parameters can be defined using Optional from typing module
@app.get('/blog')
def blog_list(limit=10, published:bool=True, sort: Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}
    
# we need to write this above the dynamic route, else it will be treated as a dynamic route
# since fastapi matches routes from top to bottom, it can match blog/xyz to blog/{id}
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

# create a dynamic route with path parameter
@app.get('/blog/{id}')
# id: int means id is an integer
def blog(id: int):
    return {'data': f'Blog post with id {id}'}

# if a param is accepted and is in path then FASTAPI knows it's a path param
# if a param is not in path then it's a query param
@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': f'Comments for blog post with id {id}'}