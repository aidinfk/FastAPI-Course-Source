from services.user import UserService
from fastapi import Request # type: ignore
# from functools import lru_cache

# @lru_cache
# def get_user_service():
#     return UserService()

def get_user_service(request: Request):
    return request.app.state.user_service