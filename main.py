from fastapi import FastAPI

app = FastAPI()

3


@app.get('/')
def index():
    return {'data':'Blog List'}

@app.get('/blog/id')
def show():
    return {'data': id}