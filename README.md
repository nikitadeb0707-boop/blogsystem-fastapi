# FastAPI Social Media Backend

A social-media-style REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, with JWT authentication, user-specific authorization, database relationships, and Alembic migrations.

This was my first backend service and my first experience deploying a backend application beyond localhost.

The project was built while following along with **Sanjeev Thiyagarajan's FastAPI course**, with the goal of learning how the different components of a backend service fit together and getting hands-on experience with deployment and database management.

---

## Features

### Authentication & Authorization

- User registration
- User authentication
- JWT-based authentication
- Password hashing
- Authenticated user identification
- User-specific authorization for protected operations

The API continuously verifies the authenticated user when performing user-specific actions, ensuring that users can only perform operations they are authorized to perform.

### Posts

- Create posts
- Retrieve posts
- Update posts
- Delete posts
- Associate posts with their creators
- Retrieve post-related user information

### Voting

- Users can like posts created by other users
- Prevents invalid/duplicate voting operations
- Votes are associated with both the user and the post

### Database

The application currently uses three main tables:

- `users` — stores user information
- `posts` — stores posts and their creators
- `votes` — stores relationships between users and posts they have liked

The project uses SQLAlchemy relationships and joins to work with related data.

### Database Migrations

- Alembic for database schema migrations
- Migration scripts for managing changes to the database schema
- PostgreSQL as the production database

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend web framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| Pydantic | Data validation and schemas |
| JWT | Authentication |
| OAuth2 | Authentication flow |
| Postman | API testing |
| Git & GitHub | Version control |
| Render | Deployment |

---

## Project Structure

```text
app/
├── alembic/
│   └── versions/          # Database migration files
│
├── routers/               # API route modules
│
├── __init__.py
├── alembic.ini            # Alembic configuration
├── config.py              # Application configuration
├── database.py            # Database connection and session
├── main.py                # FastAPI application entry point
├── models.py              # SQLAlchemy database models
├── oauth2.py              # JWT/OAuth2 authentication
├── schemas.py             # Pydantic schemas
└── utils.py               # Utility functions

.gitignore
requirements.txt
