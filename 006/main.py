from fastapi import FastAPI, status, HTTPException # type: ignore
from schemas import UserRequest, UserResponse, UserOutput
from typing import List

app = FastAPI()

users = []

@app.get("/")
def hello_user():
    return {"hello":"world"}

@app.post("/user", response_model= UserResponse, status_code= status.HTTP_201_CREATED)
def create_user(user: UserRequest):
    if any(u.email == user.email for u in users):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Email already exists!"
        )

    new_user = UserOutput(
        id = len(users) + 1,
        # See the example.py file to understand why I use **user.[any method] in this line. It is worth noting that the model_dump method converts the user object into JSON format.
        **user.model_dump()
    )
    users.append(new_user)
    return {"message": "User created", "user": new_user}

@app.get("/user", response_model= List[UserOutput])
def get_users():
    return users