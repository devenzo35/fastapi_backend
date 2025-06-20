from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    age: int


class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True
