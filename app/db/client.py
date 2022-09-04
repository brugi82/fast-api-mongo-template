from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.environ["FAMT_MONGO_URL"])

db = client["fastapi-mongo-template"]


async def get_server_info():
    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to server")
