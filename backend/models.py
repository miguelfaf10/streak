from sqlalchemy import Column, ForeignKey, Integer, String, Date, Interval
from sqlalchemy.orm import relationship
from backend.db import Base


class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    email = Column(String)


class ActivityModel(Base):
    __tablename__ = "activities"

    activity_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String)
    description = Column(String)
    color = Column(String)


class ActivityRecordModel(Base):
    __tablename__ = "activities_records"

    record_id = Column(
        Integer, primary_key=True, autoincrement=True, index=True, unique=True
    )
    user_id = Column(Integer, ForeignKey("users.user_id"))
    activity_id = Column(Integer, ForeignKey("activities.activity_id"))
    date = Column(Date)
    duration = Column(Integer)
