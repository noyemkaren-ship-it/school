from fastapi import APIRouter, Response, Form, Request
from database.UserRepository import UserRepository
from database.DataRepository import DataRepository
from schemas.data import Data
from schemas.user import UserSchema
import random
import urllib.parse

user_repo = UserRepository()
data_repo = DataRepository()
router = APIRouter()


@router.get("/users", tags=["users"])
async def get_users():
    return user_repo.get_all()


@router.get("/datas", tags=["datas"])
async def get_datas():
    data = data_repo.get_all_data()
    random.shuffle(data)
    if data:
        return data
    return {"message": "datas is empty"}


@router.post("/data/create", tags=["datas"])
async def create_data_router(data: Data):
    data_repo.create(
        name=data.name,
        school_class=data.school_class,
        school_subject=data.school_subject,
        text=data.text
    )
    return {"message": "information added successfully"}


@router.post("/user/login", tags=['users'])
async def login(
    response: Response,
    surname: str = Form(...),
    password: str = Form(...)
):
    result = user_repo.logins(surname, password)
    if "user_id" in result:
        encoded_surname = urllib.parse.quote(surname, safe='')
        response.set_cookie(key="surname", value=encoded_surname, max_age=86400)
        return {"success": True, "message": "Вход выполнен"}
    return {"success": False, "message": "Неверная фамилия или пароль"}

@router.post("/create/user", tags=["users"])
async def create_user(response: Response, user: UserSchema):
    if user_repo.get_by_surname(user.surname):
        return {"success": False, "message": "Пользователь с такой фамилией уже существует"}

    created_user = user_repo.create(
        name=user.name,
        surname=user.surname,
        password=user.password
    )
    encoded_surname = urllib.parse.quote(user.surname, safe='')
    response.set_cookie(key="surname", value=encoded_surname, max_age=86400)
    return {"success": True, "message": "Регистрация успешна", "user": created_user}

@router.patch("/data/update", tags=["datas"])
async def scores_update(new_scores: int, surname: str):
    if new_scores < 0:
        return {"message": "scores it cannot be a negative number"}
    user_repo.update_scores(surname, new_scores)
    return {"message": "Is sucesfull updated"}


@router.get("/data/{school_subject}/{school_class}", tags=["datas"])
async def get_english(school_class: int, school_subject: str):
    result = data_repo.get_by_subject_and_class(school_subject, school_class)
    if result:
        return result
    return {"message": "404 MATERIALS NOT FOUND"}


@router.get("/user/{user_id}", tags=["users"])
async def get_user(user_id: int):
    user = user_repo.get_by_id(user_id)
    if user:
        return user
    return {"message": "USER NOT FOUND"}


@router.get("/user_data", tags=["users"])
async def get_user_data(request: Request):
    raw_surname = request.cookies.get("surname")
    if not raw_surname:
        return {"error": "Не авторизован"}

    surname = urllib.parse.unquote(raw_surname)
    user = user_repo.get_by_surname(surname)

    if not user:
        return {"error": "Пользователь не найден"}

    return {
        "name": user.name,
        "surname": user.surname,
    }

@router.delete("/delete/user", tags=["Тоолько для админов"])
async def delete_user(user_id: int):
    user_repo.delete(user_id)
    return {'message': 'Is sucesfull'}

@router.get("/data/{subject}/all")
async def get_by_subject(subject: str):
    return data_repo.get_by_school_subject(subject)

@router.get("/data/all/{class_num}")
async def get_by_class(class_num: int):
    return data_repo.get_by_class(class_num)