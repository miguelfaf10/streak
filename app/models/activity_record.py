from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base


class ActivityRecord(Base):
    __tablename__ = "activity_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    date = Column(Date)
    status = Column(Boolean)  # True if the activity was accomplished
    user = relationship("User", back_populates="activity_records")
    activity = relationship("Activity", back_populates="activity_records")
