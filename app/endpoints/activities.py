from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.crud import create_activity
from app.db import get_db
from app.schemas import Activity, User

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_activity(
    db: db_dependency,
    current_user: user_dependency,
    create_activity_request: Activity,
):
    print("current_user: ", current_user)
    print("current_user.id: ", current_user["id"])
    if current_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated.")
    new_activity = Activity(
        name=create_activity_request.name,
        description=create_activity_request.description,
        color=create_activity_request.color,
    )
    create_activity(db=db, user_id=current_user["id"], activity=create_activity_request)
