from sqlalchemy.orm import Session
from models.user import User
from database.db import SessionLocal


class UserRepository:
    def __init__(self):
        self.db = SessionLocal()

    def close(self):
        self.db.close()

    def get_all(self):
        return self.db.query(User).all()

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_surname(self, surname: str):
        return self.db.query(User).filter(User.surname == surname).first()

    def create(self, name: str, surname: str, password: str):
        user = User(
            name=name,
            surname=surname,
            password=password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_scores(self, surname: str, new_scores: int):
        user = self.db.query(User).filter(User.surname == surname).first()
        if user:
            user.scores = new_scores
            self.db.commit()
            self.db.refresh(user)
        return user

    def delete(self, user_id: int):
        user = self.get_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def logins(self, surname: str, password: str):
        user = self.get_by_surname(surname)
        print(f"DEBUG: Найден пользователь: {user.surname if user else None}")
        print(f"DEBUG: Введенный пароль: {password}")
        print(f"DEBUG: Пароль в БД: {user.password if user else None}")
        if user and user.password == password:
            return {"user_id": user.id, "success": True}
        return {"success": False, "message": "Неверная фамилия или пароль"}