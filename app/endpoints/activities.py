from typing import Annotated
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/items/")
def read_activities(db: db_dependency):
    # Your logic here, using `db` as the session
    pass
