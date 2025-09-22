from pydantic import BaseModel, EmailStr
from enum import Enum


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponce(UserBase):
    id: int

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    username: str | None = None

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class RoleEnum(Enum):
    USER = "user"
    ADMIN = "admin"