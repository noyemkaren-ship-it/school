from sqlalchemy import Column, Integer, String
from database.db import Base


class Data(Base):
    __tablename__ = "Data"
    id = Column(Integer, primary_key=True, index=True)
    school_subject = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    text = Column(String(100), nullable=False)
    school_class = Column(Integer, default=0, nullable=False)
