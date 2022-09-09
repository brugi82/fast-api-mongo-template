from pydantic import BaseModel, Field
from ..db.model import MongoModel


class User(MongoModel):
    username: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    confirmed: bool | None = None


class UserInDb(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class CryptoConfig(BaseModel):
    secret_key: str
    algo: str
