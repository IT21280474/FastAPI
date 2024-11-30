from fastapi import FastAPI

app = FastAPI()

3


@app.get('/')
def index():
    return {'data':'Blog List'}

@app.get('/blog/{id}')
def show(id: int):
    #fatch blog with id = id
    return {'data': id}


@app.get('/blog/unpublished')
def comments():
    
    return{'data':'all unpublished  blogs'}



@app.get('/blog/{id}/comments')
def comments(id):
    #fatch comments of blog with id = id
    return{'data':{'1','2'}}