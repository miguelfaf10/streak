import os

FASTAPI_DEBUG_MODE = os.getenv("FASTAPI_DEBUG_MODE", "False").lower() in ["true", "1"]
SECRET_KEY = os.getenv("SECRET_KEY", "YOUR-DEFAULT-SECRET-KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
