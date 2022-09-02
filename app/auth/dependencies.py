from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from .models import UserInDb
from .crypto import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
from .services import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if not user:
        raise credentials_exception
    return user


def get_current_confirmed_user(user: UserInDb = Depends(get_current_user)):
    if user.confirmed == False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please confirm your email address",
        )
    return user


def create_access_token(data: dict, expires_delta: timedelta | None):
    copied_data = data.copy()
    if expires_delta:
        exp = datetime.utcnow() + expires_delta
    else:
        exp = datetime.utcnow() + timedelta(minutes=15)
    copied_data.update({"exp": exp})
    encoded_token = jwt.encode(copied_data, SECRET_KEY, ALGORITHM)
    return encoded_token


def create_user_access_token(user: UserInDb):
    claims = {"sub": user.username}
    access_token = create_access_token(
        claims, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return access_token
