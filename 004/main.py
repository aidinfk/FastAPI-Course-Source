from fastapi import FastAPI # type: ignore
from schemas import UserRequest, UserResponse


app = FastAPI()

@app.get("/")
def hello_user():
    return {"hello":"world"}

@app.post("/user", response_model = UserResponse)
def create_user(user: UserRequest):
    return {"message": "User created", "user": user}