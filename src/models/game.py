from src.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, BigInteger, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User


class Game(Base):
    __tablename__ = "game"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete = "CASCADE"))

    point: Mapped[int] = mapped_column(Integer, default=0)
    tie: Mapped[int] = mapped_column(Integer, default=0)
    defeat: Mapped[int] = mapped_column(Integer, default=0)
    total: Mapped[int] = mapped_column(Integer, default=0)

    user: Mapped["User"] = relationship(back_populates="games")
