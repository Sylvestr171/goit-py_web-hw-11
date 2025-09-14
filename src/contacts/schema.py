from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import date


PhoneStr = Annotated[str, StringConstraints(pattern=r'^\+380\d{9}$')] #номер у форматі +380XXXXXXXXX

class Contact(BaseModel):
    first_name: str
    last_name: str
    e_mail: EmailStr
    phone: PhoneStr
    birth_date: date
    additional_info: str | None = None


class ContactResponse(Contact):
    id: int

    class Config:
        from_attributes = True


class ContactCreate(Contact):
    pass

class ContactUpdate(Contact):
    pass

class ContactDeletedResponse(BaseModel):
    detail: str
    contact: ContactResponse
