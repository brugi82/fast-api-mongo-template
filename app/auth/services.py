from .models import UserInDb
from .crypto import verify_password

fake_user_db = {
    "test@fly.io": {
        "username": "test@fly.io",
        "first_name": "John",
        "last_name": "Doe",
        "hashed_password": "$2b$12$6VPYp77bBEF82S8wYzk/su20cU8HqZacE/K7gcJWEsKwubVNuOevu",
        "confirmed": True,
    }
}


def get_user(username):
    if username in fake_user_db:
        user = fake_user_db[username]
        return UserInDb(**user)
    return None


def authenticate_user(username, password):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
