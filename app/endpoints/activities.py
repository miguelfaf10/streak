from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.auth import get_current_user
import app.crud as crud
from app.db import get_db
from app.schemas import Activity

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_activity(
    db: db_dependency,
    current_user: user_dependency,
    create_activity_request: Activity,
):
    if current_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated.")

    crud.create_activity(
        db=db, user_id=current_user["id"], activity=create_activity_request
    )


@router.get("/", status_code=status.HTTP_200_OK)
async def activities(db: db_dependency, current_user: user_dependency):

    if current_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated.")

    activities_db = crud.get_activities(db=db, user_id=current_user["id"])
    activities = crud.transform_activities(activities_db)

    return {"Activities": activities}


@router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_activity(db: db_dependency, current_user: user_dependency, activity_id: int):

    if current_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated.")

    db_activityrecord = crud.delete_activity(
        db, activity_id=activity_id, user_id=current_user["id"]
    )

    if db_activityrecord is None:
        raise HTTPException(status_code=404, detail="Activity record not found")
