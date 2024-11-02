from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def main_page():
    return "Главная страница"


@app.get("/users")
async def get_all_users() -> list[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_new_user(username: str, age: int):
    user_id = int((users[-1].id + 1) if users else 1)
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: int, username: str, age: int):
    try:
        user = next(user for user in users if user.id == user_id)
        user.username = username
        user.age = age
        return f"User {user_id} has been update"
    except:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        user_index = next(index for index, user in enumerate(users) if user.id == user_id)
        users.pop(user_index)
        return f"User {user_id} has been deleted"
    except:
        raise HTTPException(status_code=404, detail="User was not found")
