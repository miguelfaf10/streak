from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base


class UserModel(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)


class Activity(Base):
    __tablename__ = "activities"

    name = Column(String, primary_key=True, index=True)
    description = Column(String)
    color = Column(String)


class ActivityRecord(Base):
    __tablename__ = "activity_records"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True, index=True)
    activity_name = Column(Integer, ForeignKey("activities.name"))
    date = Column(Date)
