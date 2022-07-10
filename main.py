from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import uvicorn

app = FastAPI()  # Instance of the FastAPI


@app.get('/')  # decorator
def index():
    return {"data": {"name": "John Doe", "age": 25}}


@app.get('/about')
def about():
    return {"Page": "About Page"}


@app.get('/blog')
# Query Parameters
def q_params(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": {f"{limit} Published blogs."}}
    else:
        return {"data": {f'{limit} blogs per page'}}


def blog():
    return {"data": {"blog": 1, "blog": 2, "blog": 3}}


@app.get('/blog/published')
def published_blogs():
    return {"data": {"blog": 234}}


@app.get('/blog/{id}')
def show(id: int):
    return {"data": {"blog": id}}

# POST METHOD


class Blog(BaseModel):  # Inheritance
    title: str
    body: str
    Published: bool


@app.post('/create')
def create(request: Blog):
    return (f"{request.title} Blog Created Successfully!")

# Port and Local Host Config
# if __name__ == "__main__":
#     uvicorn.run(app, host = "127.0.0.1", port = 9000)
