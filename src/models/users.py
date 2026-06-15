from src.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BigInteger, Integer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .game import Game


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    
    first_name: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    phone: Mapped[str] = mapped_column(String)          
    location: Mapped[str] = mapped_column(String)


    games: Mapped["Game"] = relationship(back_populates="user")