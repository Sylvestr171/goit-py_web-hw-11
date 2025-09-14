from sqlalchemy import select

from src.contacts.models import Contact
from src.contacts.schema import ContactCreate

class ContactReposetory:

    def __init__(self, session):
        self.session = session

    async def get_contact(self, contact_id: int) -> Contact:
        query = select(Contact).where(Contact.id == contact_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    

    async def get_all_contact(self) -> Contact:
        query = select(Contact)
        result = await self.session.execute(query)
        return result.scalars().all()
    

    async def create_contact(self, contact: ContactCreate) -> Contact:
        new_contact = Contact(**contact.model_dump())
        self.session.add(new_contact)
        await self.session.commit()
        await self.session.refresh(new_contact)
        return new_contact