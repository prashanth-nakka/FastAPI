from fastapi import FastAPI
from typing import Optional

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
