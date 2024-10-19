from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from . import Base


class Stat(Base):
    value: Mapped[int] = mapped_column(Integer, default=100)
    name: Mapped[str] = mapped_column(String(50))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"))
