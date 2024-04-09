from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db import Base
from app.crud import get_users
from app.db import get_db
import pytest
from os.path import exists
from app.models import User


if exists("streak.db"):
    print("## test_db: Database exists")
else:
    print("## test_db: Database does not exists")


# SQLALCHEMY_DATABASE_URL = "sqlite:///test.sqlite"
SQLALCHEMY_DATABASE_URL = "sqlite:///test.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


if exists("streak.db"):
    print("## test_db: Database exists")
else:
    print("## test_db: Database does not exists")


def override_get_db():
    try:
        # Create all tables in the database (this should be aligned with your models)
        Base.metadata.create_all(bind=engine)

        # Create a new database session
        db = TestingSessionLocal()

        print("Using the overriden databse")

        # Begin a transaction
        db.begin()
        yield db
    finally:
        db.rollback
        db.close()


app.dependency_overrides[get_db] = override_get_db

# create test instance of FastAPI app client
client = TestClient(app)


def test_create_user():
    if exists("streak.db"):
        print("## create_user: Database exists")
    else:
        print("## create_user: Database does no exist")

    db = next(override_get_db())
    client = TestClient(app)

    client.post(
        "/api/v1/users/",
        json={
            "email": "user1@example.com",
            "password": "password1",
        },
    )
    client.post(
        "/api/v1/users/",
        json={
            "email": "user2@example.com",
            "password": "password2",
        },
    )
    items = get_users(db, 0, 10)
    assert len(items) == 2


# def test_create_user(create_user):
#     if exists("streak.db"):
#         print("## test_creater_user: Database exists")
#     else:
#         print("## test_creater_user: Database does not exist")

#     response = client.post(
#         "/api/v1/users/",
#         json={
#             "email": "custom1@example.com",
#             "password": "password",
#         },
#     )
#     assert response.status_code == 201
#     assert response.json()["email"] == "custom1@example.com"


# def test_read_user(create_user):
#     # Create users
#     # user1, user2 = create_user
#     # Fetch the user
#     response = client.get(f"/api/v1/users/1")
#     assert response.status_code == 200
#     assert response.json()["email"] == "user1@example.com"


# def test_read_users(create_user):
#     # Create users
#     # user1, user2 = create_user
#     # Fetch users
#     response = client.get("/api/v1/users/")
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) >= 2  # Ensure at least two users are present
#     assert data[0]["email"] == "user1@example.com"
#     assert data[1]["email"] == "user2@example.com"


# def test_create_and_read_user_1(create_user):
#     # Create user
#     create_response = client.post(
#         "/api/v1/users/",
#         json={"email": "user_new@example.com", "password": "password1"},
#     )
#     assert create_response.status_code == 201
#     user_id = create_response.json()["id"]

#     # Read user
#     read_response = client.get(f"/api/v1/users/{user_id}")
#     assert read_response.status_code == 200
#     assert read_response.json()["email"] == "user_new@example.com"
