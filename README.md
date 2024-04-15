# App Mission statement

- Keep on track daily activities goals
- Help with motivation and responsability
- Be simple with minimum clutter

# Project structure

Explanation:

- /alembic: Contains Alembic configurations and migration files. Alembic is used for handling database migrations.
- /app: The main application package.
  -- /api: Contains API routes and endpoints. Organized by version (e.g., v1) for future scalability.
  -- /core: Configuration files and other core components of the application.
  -- /crud: Functions for Create, Read, Update, and Delete operations.
  -- /db: Database-related modules, including session management and initialization.
  -- /models: SQLAlchemy models representing database tables.
  -- /schemas: Pydantic schemas for request and response validation.
- /tests: This directory holds the test suite, organized similarly to the application structure.
- main.py: Entry point of the FastAPI application.
- requirements.txt: Lists all Python dependencies for your project.

Authentication and Security

- Following tutorial in: https://www.youtube.com/watch?v=0A_GCXBCNUQ
- Installed:
  - pip install "python-jose[cryptography]"
  - pip install python-multipart
  - pip install "passlib[bcrypt]"

# Front-end

- Based on React + Bootstrap
- Project created using `npx`
- Used libraries:
  - axios: for API connection

References: https://www.youtube.com/watch?v=0zb2kohYZIM&t=0s
# learning-react
