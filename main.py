from fastapi import FastAPI

app = FastAPI()  # Instance of the FastAPI


@app.get('/')  # decorator
def index():
    return {"data": {"name": "John Doe", "age": 25}}


@app.get('/about')
def about():
    return {"Page": "About Page"}
