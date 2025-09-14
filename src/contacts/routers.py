from typing import List
from fastapi import  APIRouter, Depends, HTTPException, status
from config.db import get_db
from src.contacts.repo import ContactReposetory
from src.contacts.schema import Contact, ContactCreate, ContactDeletedResponse, ContactResponse
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/", response_model=ContactResponse)
async def create_contact(contact: ContactCreate, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    return await contact_repo.create_contact(contact)

@router.get("/all", response_model=List[ContactResponse])
async def get_all_contacts(db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    return await contact_repo.get_all_contact()

@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    contact = await contact_repo.get_contact(contact_id)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.delete("/{contact_id}", response_model=ContactDeletedResponse)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    contact = await contact_repo.delete_contact(contact_id)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return {
    "detail": "Contact deleted successfully",
    "contact": contact
            }