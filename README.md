# FastAPI

This Repo provides complete information about python FASTAPI api developing framework from scrtach.


# Commands required

# for Creating a Virtual Env.
--> python -m venv <name_of_the_folder>

# To activate created Virtual Env.
--> <name_of_the_folder>\scripts\activate.bat

# To RUN the Server
--> uvicorn main:app --reload



@app.get('/') --> routing/end-points/decorators
# When we declare a dynamic parameter in the decorator, it should be called below the matching decorator.

Eg:
# matching decorator or route
@app.get('/blog/published')
def published_blogs():
    return {"data": {"blog": 234, "blog": 345}}

# Dynamically declared parameter
@app.get('/blog/{id}')
def show(id: int):
    return {"data": {"blog": id}}


# To go to Automatic generated FastAPI documentation in Swagger UI
--> http://127.0.0.1:8000/docs