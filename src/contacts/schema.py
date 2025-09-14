from typing import Annotated, Optional
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
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    e_mail: Optional[EmailStr] = None
    phone: Optional[PhoneStr] = None
    birth_date: Optional[date] = None
    additional_info: Optional[str] = None

class ContactDeletedResponse(BaseModel):
    detail: str
    contact: ContactResponse
