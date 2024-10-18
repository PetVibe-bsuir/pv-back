from sqlalchemy import Column, ForeignKey, Table, Integer

from . import Base

association_table = Table(
    "pet_achievements",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("pet_id", ForeignKey("pets.id")),
    Column("achievement_id", ForeignKey("achievements.id")),
)
