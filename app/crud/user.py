from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = UserModel(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_users(db: Session, skip: int, limit: int):
    return db.query(UserModel).offset(skip).limit(limit).all()
