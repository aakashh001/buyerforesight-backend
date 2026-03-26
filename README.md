# User Management API

This project implements a RESTful API for managing users using FastAPI.

It demonstrates API design, data handling, validation, and clean architecture.

---

## Features

- Create user
- Get users
- Update user
- Delete user
- Search users
- Sort users

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- JSON file storage

---

## Python Version

Python 3.10+

---

## Installation

pip install -r requirements.txt

---

## Run the Application

uvicorn main:app --reload

---

## API Documentation

Swagger UI:

https://buyerforesight-backend-qon8.onrender.com/docs

---

## Deployment

https://buyerforesight-backend-qon8.onrender.com

---

## API Endpoints

GET /users  
GET /users/{id}  
POST /users  
PUT /users/{id}  
DELETE /users/{id}

---

## Data Storage

User data is stored in a JSON file (users.json).

---

## Error Handling

The API uses FastAPI's HTTPException to handle errors.

Examples:

404 – User not found  
422 – Validation error  

---

## Project Structure

buyerforesight-backend/

main.py – API routes  
models.py – Pydantic schemas  
database.py – JSON file operations  
users.json – Data storage  

---

## Assumptions

- User IDs are auto-incremented
- Data is stored locally in a JSON file
- API is designed for demonstration purposes
