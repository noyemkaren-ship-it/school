from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    surname: str
    password: str