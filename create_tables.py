from sqlalchemy import create_engine
from database.db import Base, engine
from models.data import Data
from models.user import User

def init_db():
    Base.metadata.create_all(bind=engine)

init_db()