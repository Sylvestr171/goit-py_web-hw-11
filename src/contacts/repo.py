from sqlalchemy import select

from src.contacts.models import Contact
from src.contacts.schema import ContactCreate

class ContactReposetory:

    def __init__(self, session):
        self.session = session

    async def get_contact(self, contact_id: int) -> Contact:
        query = select(Contact).where(contact_id == contact_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    

    async def create_contact(self, contact: ContactCreate) -> Contact:
        new_contact = Contact(**contact.model_dump())
        self.session.add(new_contact)
        await self.session.commit()
        await self.session.refresh(new_contact)
        return new_contact