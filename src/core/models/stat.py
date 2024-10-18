from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import time

from . import Base


class Stat(Base):
    value: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(50))
    updated_at: Mapped[int] = mapped_column(
        Integer, default=lambda: int(time.time() * 1000)
    )
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"))
