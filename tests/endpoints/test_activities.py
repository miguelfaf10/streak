# test_activities.py

import pytest
from fastapi.testclient import TestClient
from app.main import app  # replace with the path to your FastAPI application
from app.schemas import Activity
import app.crud as crud

client = TestClient(app)


def test_create_activity():
    # Arrange
    test_activity = Activity(name="Test Activity", unit="Test Unit")
    test_user = {"id": 1}  # replace with a test user
    crud.create_activity = MagicMock()  # mock the create_activity function

    # Act
    response = client.post(
        "/activities/",  # replace with the path to your new_activity route
        json=test_activity.dict(),
        headers={
            "Authorization": f"Bearer {test_user['id']}"
        },  # replace with your authentication method
    )

    # Assert
    assert response.status_code == 201
    crud.create_activity.assert_called_once_with(
        db=ANY, user_id=test_user["id"], activity=test_activity
    )


def test_get_activities():
    # Arrange
    test_user = {"id": 1}  # replace with a test user
    crud.get_activities = MagicMock()  # mock the get_activities function
    crud.transform_activities = MagicMock()  # mock the transform_activities function

    # Act
    response = client.get(
        "/activities/",  # replace with the path to your activities route
        headers={
            "Authorization": f"Bearer {test_user['id']}"
        },  # replace with your authentication method
    )

    # Assert
    assert response.status_code == 200
    crud.get_activities.assert_called_once_with(db=ANY, user_id=test_user["id"])
    crud.transform_activities.assert_called_once()
