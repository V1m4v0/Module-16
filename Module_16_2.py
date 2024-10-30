from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user(user_id: Annotated[str, Path(min_length=1, max_length=100, description='Enter User ID', example='24')] ):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def full_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Vimavo')]
                    , age: Annotated[int, Path(min_length=18, max_length=120, description='Enter age', example='22')]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."
