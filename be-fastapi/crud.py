from sqlalchemy.orm import Session
from app.models import ActivityRecordModel, UserModel, ActivityModel
from app.schemas import ActivityRecord, User, Activity


## CRUD operations for Users
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


## CRUD operations for Activities
def activity_exists(db: Session, activity_id: int, user_id: int):
    existing_activities = get_activities(db, user_id)
    existing_activities_ids = [activity.activity_id for activity in existing_activities]
    return activity_id in existing_activities_ids


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


def get_activities(db: Session, user_id: int):
    return db.query(ActivityModel).filter(ActivityModel.user_id == user_id).all()


def delete_activity(db: Session, user_id: int, activity_id: int):

    activity_records = (
        db.query(ActivityRecordModel)
        .filter(
            ActivityRecordModel.activity_id == activity_id,
            ActivityRecordModel.user_id == user_id,
        )
        .delete(synchronize_session=False)
    )

    activity = (
        db.query(ActivityModel)
        .filter(
            ActivityModel.activity_id == activity_id,
            ActivityModel.user_id == user_id,
        )
        .first()
    )
    if activity is None:
        return None
    db.delete(activity)
    db.commit()
    return activity


def transform_activities(activities_db):
    return [Activity(**activity_db.__dict__) for activity_db in activities_db]


## CRUD operations for Activity Records
def create_activityrecord(
    db: Session,
    user_id: int,
    activityrecord: ActivityRecord,
):
    db_activityrecord = ActivityRecordModel(
        activity_id=activityrecord.activity_id,
        date=activityrecord.date,
        duration=activityrecord.duration,
        user_id=user_id,
    )
    db.add(db_activityrecord)
    db.commit()
    db.refresh(db_activityrecord)
    return db_activityrecord


def get_activitiesrecords(db: Session, user_id: int):
    return (
        db.query(ActivityRecordModel)
        .filter(ActivityRecordModel.user_id == user_id)
        .all()
    )


def delete_activityrecord(db: Session, record_id: int, user_id: int):
    activity_record = (
        db.query(ActivityRecordModel)
        .filter(
            ActivityRecordModel.record_id == record_id,
            ActivityRecordModel.user_id == user_id,
        )
        .first()
    )
    if activity_record is None:
        return None
    db.delete(activity_record)
    db.commit()
    return activity_record


def transform_activities_records(activitiesrecords_db: list[ActivityRecordModel]):
    return [
        ActivityRecord(**activityrecord_db.__dict__)
        for activityrecord_db in activitiesrecords_db
    ]
