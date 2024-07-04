from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello world this is azure containers'}   