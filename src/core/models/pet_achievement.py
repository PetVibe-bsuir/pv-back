from sqlalchemy import Column, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from . import Base


class PetAchievement(Base):
    __tablename__ = "pet_achievements"
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"))
    achievement_id: Mapped[int] = mapped_column(ForeignKey("achievements.id"))
    achieved_in: Mapped[datetime] = mapped_column(server_default=func.now())
