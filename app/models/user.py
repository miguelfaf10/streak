from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base  # Assuming base.py contains the declarative base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    activity_records = relationship("ActivityRecord", back_populates="user")
