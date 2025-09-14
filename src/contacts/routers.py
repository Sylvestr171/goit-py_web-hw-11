from typing import List
from fastapi import  APIRouter, Depends, HTTPException, status
from pydantic import EmailStr
from config.db import get_db
from src.contacts.repo import ContactReposetory
from src.contacts.schema import Contact, ContactCreate, ContactDeletedResponse, ContactResponse, ContactUpdate
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

@router.get("/birthday_in_week", response_model=List[ContactResponse])
async def get_birthdays_next_7_days(db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    contact = await contact_repo.get_birthdays_next_7_days()
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    contact = await contact_repo.get_contact(contact_id)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.patch("/{contact_id}", response_model=ContactResponse)
async def update_contact_partial(contact_id: int, contact_update: ContactUpdate, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    existing_contact = await contact_repo.get_contact(contact_id)

    if not existing_contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    update_data = contact_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_contact, key, value)

    await db.commit()
    await db.refresh(existing_contact)
    
    return existing_contact

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

@router.get("/first_name/{firs_name}", response_model=List[ContactResponse])
async def get_contact_first_name(firs_name: str, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    contact = await contact_repo.get_contact_first_name(firs_name)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.get("/last_name/{last_name}", response_model=List[ContactResponse])
async def get_contact_last_name(last_name: str, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    contact = await contact_repo.get_contact_last_name(last_name)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.get("/e_mail/{e_mail}", response_model=List[ContactResponse])
async def get_contact_e_mail(e_mail: EmailStr, db: AsyncSession = Depends(get_db)):
    contact_repo = ContactReposetory(db)
    contact = await contact_repo.get_contact_e_mail(e_mail)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact