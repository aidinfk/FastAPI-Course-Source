from services.user import UserService
from functools import lru_cache

@lru_cache
def get_user_service():
    return UserService()