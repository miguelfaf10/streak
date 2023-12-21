from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL, adjust for your database (SQLite for development)
SQLALCHEMY_DATABASE_URL = "sqlite:///./streak.db"

# Create the SQLAlchemy engine
# For SQLite, add connect_args={"check_same_thread": False}
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal class will be used to create sessions for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
