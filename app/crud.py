from sqlalchemy.orm import Session
from app.models import UserModel, ActivityModel
from app.schemas import User, Activity


## CRUD operations for User
def create_user(db: Session, user: User):
    print("USER: ", user)
    db_user = UserModel(
        username=user.username, hashed_password=user.password, email=user.email
    )
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


## CRUD operations for Activity
def create_activity(
    db: Session,
    user_id: int,
    activity: Activity,
):
    db_activity = ActivityModel(
        name=activity.name,
        description=activity.description,
        color=activity.color,
        user_id=user_id,
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    print(db_activity)
    return db_activity
