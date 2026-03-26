from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import User, CreateUser, UpdateUser
from database import read_users, write_users

app = FastAPI(
    title="User Management API",
    description="BuyerForeSight Backend Assignment",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "BuyerForesight API is running"}
@app.get("/health")
def health():
    return {"status": "ok"}
# GET /users
@app.get("/users", response_model=List[User])
def get_users(
    search: Optional[str] = None,
    sort: Optional[str] = None,
    order: str = "asc"
):

    users = read_users()

    # Search
    if search:
        users = [
            user for user in users
            if search.lower() in user["name"].lower()
        ]

    # Sorting
    if sort:
        reverse = order == "desc"
        users.sort(
            key=lambda x: x.get(sort),
            reverse=reverse
        )

    return users


# GET /users/:id
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):

    users = read_users()

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# POST /users
@app.post("/users", response_model=User)
def create_user(user: CreateUser):

    users = read_users()

    new_id = 1

    if users:
        new_id = max(u["id"] for u in users) + 1

    new_user = {
        "id": new_id,
        **user.dict()
    }

    users.append(new_user)

    write_users(users)

    return new_user


# PUT /users/:id
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated: UpdateUser):

    users = read_users()

    for index, user in enumerate(users):

        if user["id"] == user_id:

            if updated.name is not None:
                user["name"] = updated.name

            if updated.email is not None:
                user["email"] = updated.email

            if updated.age is not None:
                user["age"] = updated.age

            users[index] = user

            write_users(users)

            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# DELETE /users/:id
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    users = read_users()

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            write_users(users)

            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )