from datetime import timedelta, datetime

from starlette import status
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List, Annotated
from app.db import get_db
from app.crud import create_user, authenticate_user
from app.schemas import User
from app.auth import (
    get_current_user,
    hash_password,
    authenticate_user,
    create_access_token,
)

from app.schemas import Token

from app.db import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/users", status_code=status.HTTP_200_OK)
async def user(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=404, detail="Authentication failed.")
    return {"User": user}


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def new_user(db: db_dependency, user: User):
    print("USER: ", user)
    create_user_hashed = User(
        username=user.username,
        password=hash_password(user.password),
        email=user.email,
    )
    print("USER: ", create_user_hashed)
    create_user(db=db, user=create_user_hashed)


@router.post("/token", response_model=Token)
async def login_for_access_token(
    db: db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):

    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(user.username, user.user_id, timedelta(minutes=20))

    return {"access_token": token, "token_type": "bearer"}


# @router.get("/{user_id}", response_model=User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     print("Reading Single User")
#     db_user = get_user_by_id(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.get("/all", response_model=List[User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     print("Reading Users")
#     users = get_users(db, skip=skip, limit=limit)
#     return users
