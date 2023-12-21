from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.api.v1.deps import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///test.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        Base.metadata.create_all(bind=engine)
        db = TestingSessionLocal()
        db.begin()
        yield db
    finally:
        db.rollback()
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "user@example.com",
            "password": "password",
        },
    )
    assert response.status_code == 201
    assert response.json()["email"] == "user@example.com"


def test_read_user():
    # Set up by creating a user through the API
    client.post(
        "/api/v1/users/", json={"email": "user@example.com", "password": "password"}
    )

    response = client.get("/api/v1/users/1")
    print(response)
    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"


def test_read_users():
    # Set up by creating a user through the API
    client.post(
        "/api/v1/users/", json={"email": "user1@example.com", "password": "password1"}
    )
    client.post(
        "/api/v1/users/", json={"email": "user2@example.com", "password": "password1"}
    )

    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert response.json()[0]["email"] == "user1@example.com"
    assert response.json()[1]["email"] == "user2@example.com"


def test_create_and_read_user_1():
    # Create user
    create_response = client.post(
        "/api/v1/users/", json={"email": "user1@example.com", "password": "password1"}
    )
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]

    # Read user
    read_response = client.get(f"/api/v1/users/{user_id}")
    assert read_response.status_code == 200
    assert read_response.json()["email"] == "user1@example.com"
