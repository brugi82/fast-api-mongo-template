from pydantic import BaseModel


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    confirmed: bool | None = None


class UserInDb(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str
