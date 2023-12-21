from fastapi import FastAPI
from app.api.v1.endpoints import users, activities, activity_records
from app.db.session import engine
from app.db.base import Base  # This is to ensure models are imported
from app.models.user import User
from app.models.activity import Activity
from app.models.activity_record import ActivityRecord

# Create all tables in the database.
# Comment this out if you are using Alembic for migrations.
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes from different endpoints
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(activities.router, prefix="/api/v1/activities", tags=["activities"])
app.include_router(
    activity_records.router,
    prefix="/api/v1/activity_records",
    tags=["activity_records"],
)


@app.get("/")
def read_root():
    return {"App": "Streak Calendar"}
