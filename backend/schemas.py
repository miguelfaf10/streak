from datetime import date, timedelta
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


class ActivityOut(BaseModel):
    activity_id: int
    name: str
    description: Optional[str] = "no description"
    color: str

class ActivityRecord(BaseModel):
    activity_id: int
    date: date
    duration: Optional[int] = 0
