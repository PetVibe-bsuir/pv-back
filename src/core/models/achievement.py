from sqlalchemy import Integer, Text, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
import time

from . import Base


class Achievement(Base):
    exp: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(Text)
    updated_at: Mapped[int] = mapped_column(
        Integer, default=lambda: int(time.time() * 1000)
    )
