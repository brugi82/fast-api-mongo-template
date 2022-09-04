from passlib.context import CryptContext
import os

SECRET_KEY = os.environ["FAMT_SECRET_KEY"]
ALGORITHM = os.environ["FAMT_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"])


def verify_password(password, hashed_password):
    print(f"{password}: {pwd_context.hash(password)}")
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
