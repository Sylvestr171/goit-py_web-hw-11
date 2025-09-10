from fastapi import  APIRouter
from src.contacts.schema import Contact, ContactResponse

router = APIRouter()

@router.get("/all")
async def get_contacts():
    return {"contacts":"all contacts"}

@router.get("/{contact_id}")
async def get_contact(contact_id: int):
    return {"contact_id":contact_id}

# @router.post("/contacts")
# async def create_contact(contact: Contact):
#     return {"name": (contact.first_name, contact.last_name), "birth day": contact.birth_date}

@router.post("/")
async def create_contact(contact: Contact) -> ContactResponse:
    return ContactResponse(first_name=contact.first_name, last_name=contact.last_name)