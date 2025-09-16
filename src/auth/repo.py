from pydantic import EmailStr
from sqlalchemy import select

from src.contacts.schema import UserCreate

class UserReposetory:

    def __init__(self, session):
        self.session = session


    async def create_user(self, user_create: UserCreate):
        hash_password = get_password_hash (user_create.password)
        new_user = User(
            username = user_create.username,
            hashed_password = hashed_password,
            email = user_create.email,
        )
        self.session.commit(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user