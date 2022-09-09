from fastapi import FastAPI
from .auth.router import router as auth_router
from app.db.client import init_db
import sys

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
async def root():
    return "Hello world!"


@app.get("/test")
async def test():
    return "Testing 123"


if "pytest" not in sys.modules:
    init_db()
