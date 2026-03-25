from pydantic import BaseModel

class Data(BaseModel):
    school_subject: str
    name: str
    text: str
    school_class: int


