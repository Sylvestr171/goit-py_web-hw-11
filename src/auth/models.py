from config.db import Base

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship



class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password:  Mapped[str] = mapped_column(String)
    # is_active: Mapped[bool] = mapped_column(default=True)
    contacts: Mapped[list["Contact"]] = relationship("Contact", back_populates="owner")