from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from . import Base

if TYPE_CHECKING:
    from . import Pet


class User(Base):
    username: Mapped[str] = mapped_column(String(50))
    pet: Mapped["Pet"] = relationship(back_populates="user")
