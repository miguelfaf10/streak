from sqlalchemy.orm import Session
from app.models import UserModel
from app.schemas import CreateUserRequest


def create_user(db: Session, user: CreateUserRequest):
    db_user = UserModel(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        return False
    if not user.hashed_password == password:
        return False
    return user


def get_user(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()
