from pydantic import EmailStr
from sqlalchemy import select

from src.auth.models import User
from src.auth.pass_utils import get_password_hash
from src.auth.schema import UserCreate

class UserRepository:

    def __init__(self, session):
        self.session = session


    async def create_user(self, user_create: UserCreate):
        hash_password = get_password_hash (user_create.password)
        new_user = User(
            username = user_create.username,
            hashed_password = hash_password,
            email = user_create.email,
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user
    
    async def get_user_by_email(self, email):
        query = select(User).where(User.email == email)
        resalt = await self.session.execute(query)
        return resalt.scalar_one_or_none()