from models.data import Data
from database.db import SessionLocal


class DataRepository:
    def __init__(self):
        self.db = SessionLocal()

    def close(self):
        self.db.close()

    def get_by_subject_and_class(self, school_subject: str, school_class: int):
        return self.db.query(Data).filter(
            Data.school_subject == school_subject,
            Data.school_class == school_class
        ).all()

    def get_all_data(self):
        return self.db.query(Data).all()

    def get_by_id_data(self, data_id: int):
        return self.db.query(Data).filter(Data.id == data_id).first()

    def get_by_school_subject(self, school_subject: str):
        return self.db.query(Data).filter(Data.school_subject == school_subject).first()

    def get_by_class(self, school_class: int):
        return self.db.query(Data).filter(Data.school_class == school_class).first()

    def create(self, school_subject, name, text, school_class):
        data = Data(
            name=name,
            school_class=school_class,
            school_subject=school_subject,
            text=text
        )
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data

    def delete(self, data_id: int):
        data = self.get_by_id_data(data_id)
        if data:
            self.db.delete(data)
            self.db.commit()
            return True
        return False