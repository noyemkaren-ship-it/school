from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base


class TestResult(Base):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    test_name = Column(String(100), nullable=False)
    score = Column(Integer, default=0)
    total = Column(Integer, default=0)
    grade = Column(Integer, default=2)
    date = Column(String(50), nullable=False)