from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int


class CreateUser(BaseModel):
    name: str
    email: str
    age: int


class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None