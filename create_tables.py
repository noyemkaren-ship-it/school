from sqlalchemy import create_engine
from database.db import Base, engine
from models.user import User
from models.data import Data
from models.test_result import TestResult


def init_db():
    # Сначала создаём все таблицы
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")


if __name__ == "__main__":
    init_db()