from fastapi import APIRouter

router = APIRouter(prefix="/auth")


@router.get("/")
async def hello():
    return "Hello from auth route!"
