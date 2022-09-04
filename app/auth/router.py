from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.models import User
from .dependencies import (
    create_user_access_token,
    get_current_user,
    get_current_confirmed_user,
)
from .services import authenticate_user

router = APIRouter(prefix="/auth")


@router.post("/login")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_user_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/unprotected")
async def unprotected():
    return "This is unprotected route"


@router.get("/protected_confirmed")
async def protected_confirmed(user: User = Depends(get_current_confirmed_user)):
    return "You are on protected route with confirmed user! " + user.username


@router.get("/protected")
async def protected(user: User = Depends(get_current_user)):
    return "You are on protected route! " + user.username
