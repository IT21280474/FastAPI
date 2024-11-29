from fastapi import FastAPI

app = FastAPI()




@app.get('/')
def index():
    return {'data':{'name':'Malith'}}

@app.get('/about')
def about():
    return {'data':{'about page'}}