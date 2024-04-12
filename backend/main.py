from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.endpoints import activities, activity_records, users
from backend.db import engine
from backend.db import Base  # This is to ensure models are imported
from backend.models import UserModel
from backend.config import FASTAPI_DEBUG_MODE
import logging

logger = logging.getLogger(__name__)


# Create all tables in the database.
# Comment this out if you are using Alembic for migrations.
Base.metadata.create_all(bind=engine)

# create FastAPI application
app = FastAPI(debug=FASTAPI_DEBUG_MODE)

# Include routes from different endpoints
app.include_router(users.router, prefix="/auth", tags=["users"])
app.include_router(activities.router, prefix="/activities", tags=["activities"])
app.include_router(
    activity_records.router,
    prefix="/activity_records",
    tags=["activity_records"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"App": "Streak Calendar"}


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f"An error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred."},
    )
