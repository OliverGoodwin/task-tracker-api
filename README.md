# Task Tracker API

A simple backend API built with FastAPI that allows you to create, read, update, and delete tasks. This project uses full CRUD functionality, persistence with SQLite using SQLAlchemy, input validation with Pydantic, and a clean API structure.

This was created to learn about CRUD operations, databases, and building APIs.

## **Features**

- Create tasks with a title and completion status
- Read all tasks from the database
- Update tasks by ID
- Delete tasks by ID
- Input validation with Pydantic
- Persistent storage using SQLite
- Interactive API documentation with Swagger UI (/docs)

## **Requirements**

- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy

## **Installation**

Create virtual environment:

python -m venv venv
# Windows PowerShell
.\venv\Scripts\activate

Install dependencies:

pip install fastapi uvicorn pydantic sqlalchemy

Run the API:

uvicorn main:app --reload

Open http://127.0.0.1:8000/docs to access Swagger UI and test the API.
