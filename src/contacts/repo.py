from sqlalchemy import select

from src.contacts.models import Contact

class ContactReposetory:

    def __init__(self, session):
        self.db = session

    async def get_contact(self, contact_id: int) -> Contact:
        query = select(Contact).where(contact_id == contact_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()