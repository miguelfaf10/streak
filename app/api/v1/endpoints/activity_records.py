from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db

router = APIRouter()


@router.get("/items/")
def read_records(db: Session = Depends(get_db)):
    # Your logic here, using `db` as the session
    pass
