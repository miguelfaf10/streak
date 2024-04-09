from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class Activity(BaseModel):
    name: str
    description: Optional[str] = "no description"
    color: str
