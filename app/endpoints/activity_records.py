from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from app.auth import get_current_user
import app.crud as crud
from app.db import get_db
from app.schemas import ActivityRecord

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_activity_record(
    db: db_dependency,
    current_user: user_dependency,
    create_activityrecord_request: ActivityRecord,
):
    if current_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated.")

    existing_activities = crud.get_activities(db, user_id=current_user["id"])

    # extract activity_id from list
    existing_activities_ids = [activity.activity_id for activity in existing_activities]

    if (
        existing_activities is None
        or create_activityrecord_request.activity_id not in existing_activities_ids
    ):
        raise HTTPException(status_code=404, detail="Activity type not found")
    crud.create_activityrecord(
        db=db, user_id=current_user["id"], activityrecord=create_activityrecord_request
    )


@router.get("/", status_code=status.HTTP_200_OK)
async def activities_records(db: db_dependency, current_user: user_dependency):

    if current_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated.")
    activitiesrecords_db = crud.get_activitiesrecords(db=db, user_id=current_user["id"])

    activitiesrecords = [
        ActivityRecord(**activityrecord_db.__dict__)
        for activityrecord_db in activitiesrecords_db
    ]
    return {"ActivitiesRecords": activitiesrecords}


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_activityrecord(
    db: db_dependency, current_user: user_dependency, record_id: int
):

    if current_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated.")
    db_activityrecord = crud.delete_activityrecord(
        db, record_id=record_id, user_id=current_user["id"]
    )
    if db_activityrecord is None:
        raise HTTPException(status_code=404, detail="Activity record not found")
