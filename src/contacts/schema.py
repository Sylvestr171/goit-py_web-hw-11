from pydantic import BaseModel, EmailStr
from datetime import date

class Contact(BaseModel):
    first_name: str
    last_name: str
    e_mail: EmailStr
    birth_date: date
    additional_info: str | None = None


class ContactResponse(BaseModel):
    first_name: str
    last_name: str
