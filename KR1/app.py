from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import User, UserAge, Feedback

app = FastAPI()

user = User(
    name="Ваше Имя и Фамилия",
    id=1
)

feedbacks = []


@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}


@app.get("/html")
def get_html():
    return FileResponse("index.html")


@app.post("/calculate")
def calculate(num1: int, num2: int):
    return {"result": num1 + num2}


@app.get("/users")
def get_user():
    return user


@app.post("/user")
def check_user(user: UserAge):

    is_adult = user.age >= 18

    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }


@app.post("/feedback")
def add_feedback(feedback: Feedback):

    feedbacks.append(feedback)

    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }