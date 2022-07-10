from fastapi import FastAPI
from .schemas import Blog

app = FastAPI()  # Instance for FastAPI

# CRUD Operations

# POST METHOD

@app.post('/blog')
def create(request: Blog):
    return {"data": [f"{request.title} is created with body {request.body}"]}
