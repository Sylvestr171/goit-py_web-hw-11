from config.db import Base

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from src.contacts.models import Contact



class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password:  Mapped[str] = mapped_column(String)
    # is_active: Mapped[bool] = mapped_column(default=True)

    contacts: Mapped[list["Contact"]] = relationship("Contact", back_populates="owner")

    role_id: Mapped[int]  = mapped_column(Integer, ForeignKey("roles.id"), nullable=True)
    role: Mapped[str] = relationship("Role", lazy="selectin")


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True)
