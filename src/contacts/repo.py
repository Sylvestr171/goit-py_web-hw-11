from pydantic import EmailStr
from sqlalchemy import select

from src.contacts.models import Contact
from src.contacts.schema import ContactCreate

class ContactReposetory:

    def __init__(self, session):
        self.session = session

    async def create_contact(self, contact: ContactCreate) -> Contact:
        new_contact = Contact(**contact.model_dump())
        self.session.add(new_contact)
        await self.session.commit()
        await self.session.refresh(new_contact)
        return new_contact    
    
    async def get_all_contact(self) -> Contact:
        query = select(Contact)
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def get_contact(self, contact_id: int) -> Contact:
        query = select(Contact).where(Contact.id == contact_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def delete_contact(self, contact_id: int) -> Contact | None:
        query = select(Contact).where(Contact.id == contact_id)
        result = await self.session.execute(query)
        contact = result.scalar_one_or_none()

        if contact:
            await self.session.delete(contact)
            await self.session.commit()
            return contact
        return None
    
    async def get_contact_first_name(self, first_name: str) -> Contact:
        query = select(Contact).where(Contact.first_name == first_name)
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def get_contact_last_name(self, last_name: str) -> Contact:
        query = select(Contact).where(Contact.last_name == last_name)
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def get_contact_e_mail(self, e_mail: EmailStr) -> Contact:
        query = select(Contact).where(Contact.e_mail == e_mail)
        result = await self.session.execute(query)
        return result.scalars().all()