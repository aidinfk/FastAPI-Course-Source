from fastapi import FastAPI # type: ignore
from schemas import UserRequest


app = FastAPI()

@app.get("/")
def hello_user():
    return {"hello":"world"}

@app.post("/user")
def create_user(user: UserRequest):
    return {"message": "user created"}