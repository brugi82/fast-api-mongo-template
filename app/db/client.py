from motor.motor_asyncio import AsyncIOMotorClient
import os

client = None

db = None


def init_db():
    global client
    global db

    client = AsyncIOMotorClient(os.environ["FAMT_MONGO_URL"])
    db = client["fastapi-mongo-template"]


def get_db():
    return db


async def get_server_info():
    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to server")
