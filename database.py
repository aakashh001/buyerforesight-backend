import json
from pathlib import Path

FILE_PATH = Path("users.json")


def read_users():
    if not FILE_PATH.exists():
        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def write_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)