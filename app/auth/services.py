from app.auth.models import UserInDb
from .crypto import verify_password
from ..db.client import db, get_db


async def get_user(username):
    user = await get_db()["user"].find_one({"username": {"$eq": username}})
    if user:
        return UserInDb(**user)
    return None


async def authenticate_user(username, password):
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
