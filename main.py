from fastapi import FastAPI
from schema import Contact, ContactResponse

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message":"ping is ok"}

@app.get("/contacts/all")
async def get_contacts():
    return {"contacts":"all contacts"}

@app.get("/contacts/{contact_id}")
async def get_contact(contact_id: int):
    return {"contact_id":contact_id}

# @app.post("/contacts")
# async def create_contact(contact: Contact):
#     return {"name": (contact.first_name, contact.last_name), "birth day": contact.birth_date}

@app.post("/contacts")
async def create_contact(contact: Contact) -> ContactResponse:
    return ContactResponse(first_name=contact.first_name, last_name=contact.last_name)