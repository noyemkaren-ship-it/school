from sqlalchemy import Column, Integer, String
from database.db import Base

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    scores = Column(Integer, default=0, nullable=False)
    password = Column(String(100), nullable=False)
