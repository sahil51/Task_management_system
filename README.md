# Task Management System API

A simple Task Management REST API built with FastAPI and Pydantic.

I created this project while learning FastAPI to understand how backend applications are structured in real-world projects. The goal was to build a clean and modular API that demonstrates CRUD operations, data validation, and separation of concerns.

---

## About the Project

This API allows users to manage tasks through REST endpoints. Each task includes:

- A unique ID (UUID)
- Title
- Description
- Priority level (1 to 5)
- Completion status

The project uses an in-memory dictionary as a temporary database and follows a modular folder structure to keep routing, schemas, business logic, and data storage separate.

---

## Features

- Create a new task
- Retrieve all tasks
- Filter tasks by completion status
- Retrieve a single task by ID
- Update an existing task
- Mark a task as completed
- Delete a task

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git
- GitHub

---

## Project Structure

```text
Task_management_system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── database.py
│   ├── services.py
│   └── routers/
│       ├── __init__.py
│       └── task.py
│
├── .gitignore
└── README.md
```

## Installation

```code
git clone https://github.com/sahil51/Task_management_system.git
cd Task_management_system

python -m venv myvenv
source myvenv/Scripts/activate   # For Git Bash on Windows

pip install fastapi uvicorn[standard] pydantic
```
## Running the applications
```code
python -m uvicorn app.main:app --reload
```
## After starting the server, the application will be available at:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
## API Endpoint
| Method | Endpoint                    | Description              |
| ------ | --------------------------- | ------------------------ |
| POST   | `/tasks`                    | Create a new task        |
| GET    | `/tasks`                    | Retrieve all tasks       |
| GET    | `/tasks?completed=true`     | Retrieve completed tasks |
| GET    | `/tasks/{task_id}`          | Retrieve a task by ID    |
| PUT    | `/tasks/{task_id}`          | Update a task            |
| PATCH  | `/tasks/{task_id}/complete` | Mark a task as completed |
| DELETE | `/tasks/{task_id}`          | Delete a task            |


## What I Learned

# This project helped me practice and understand:

- REST API design
- CRUD operations
- Request and response validation
- UUID-based identifiers
- Modular project architecture
- Separation of routing and business logic
- Error handling
- Git and GitHub workflow
- 
## Future Improvements
- Database integration using SQLAlchemy and SQLite
- Authentication with JWT
- Unit testing with Pytest
- Containerization with Docker
- CI/CD automation
- Author

Sahil
GitHub: https://github.com/sahil51
