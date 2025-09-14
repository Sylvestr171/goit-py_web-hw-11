from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date

from config.db import Base



class Contact(Base):
    __tablename__ = "contact"


    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String, index=True)
    last_name: Mapped[str] = mapped_column(String, index=True)
    e_mail: Mapped[str] = mapped_column(String, unique=True, index=True)
    phone: Mapped[str] = mapped_column(String, index=True)
    birth_date: Mapped[Date] = mapped_column(Date)
    additional_info: Mapped[str | None] = mapped_column(String, nullable=True)