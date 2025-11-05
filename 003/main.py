from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_user():
    return {"hello":"world"}

# Path parameters & Query Parameters

@app.get("/user/{user_name: str}/{age: int}")
def hello_root(user_name: str, age: int):
    return {"user_name": user_name, "age": age}

@app.get("/admin")
def hello_admin(user_name: str = None, age: int = None):
    return {"user_name": user_name, "age": age}