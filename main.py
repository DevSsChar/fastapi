from fastapi import FastAPI

# create an instance of the app using FASTAPI
app=FastAPI()

# give path operation decorator, to create a route
@app.get('/')
def index():
    return {'data':{'name':'dev'}}

@app.get('/about')
def about():
    return {'data':'about page'}