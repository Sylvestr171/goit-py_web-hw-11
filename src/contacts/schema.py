from pydantic import BaseModel, EmailStr
from datetime import date

class Contact(BaseModel):
    first_name: str
    last_name: str
    e_mail: EmailStr
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
