from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # decorator
def index():
    return "Heyy!"
