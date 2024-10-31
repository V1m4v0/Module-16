from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/users")
async def get_all_users():
    return users

@app.post('/user/{username}/{age}')
async def create_new_user(username: str, age: int):
    new_user_id = str(int(max(users, key=int)) + 1)
    users[new_user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: str, username: str, age: int):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} has been update"

@app.delete('/user/{user_id}')
async def delete_user(user_id:str):
    users.pop(user_id)
    return f"User {user_id} has been deleted"

'''@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user(user_id: Annotated[str, Path(min_length=1, max_length=100, description='Enter User ID', example='24')] ):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def full_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Vimavo')]
                    , age: Annotated[int, Path(min_length=18, max_length=120, description='Enter age', example='22')]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."'''

