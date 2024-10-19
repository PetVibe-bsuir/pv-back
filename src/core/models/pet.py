from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

from .pet_achievement import PetAchievement
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .stat import Stat
    from .achievement import Achievement


class Pet(Base):
    exp: Mapped[int] = mapped_column(Integer, default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="pet")
    stats: Mapped[List["Stat"]] = relationship()
    achievement: Mapped[List["Achievement"]] = relationship(secondary=PetAchievement)
