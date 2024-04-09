from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base


class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    email = Column(String)


class ActivityModel(Base):
    __tablename__ = "activities"

    activity_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String)
    description = Column(String)
    color = Column(String)


class ActivityRecord(Base):
    __tablename__ = "activity_records"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.activity_id"))
    date = Column(Date)
