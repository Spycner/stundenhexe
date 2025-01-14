"""School model definition."""

from datetime import time
from typing import Annotated, Optional

from sqlalchemy import String, Time
from sqlalchemy.orm import mapped_column, relationship

from studenhexe.models.base import BaseModel
from studenhexe.models.types import name_type

time_type = Annotated[time, mapped_column(Time, nullable=False)]


class School(BaseModel):
    """School model representing an educational institution."""

    __tablename__ = "schools"

    name: name_type
    operating_hours_start: time_type = mapped_column(default=time(8, 0))  # 8:00 AM
    operating_hours_end: time_type = mapped_column(default=time(16, 0))  # 4:00 PM
    period_duration: Annotated[int, mapped_column(nullable=False)] = mapped_column(
        default=45
    )  # minutes
    break_duration: Annotated[int, mapped_column(nullable=False)] = mapped_column(
        default=10
    )  # minutes
    description: Optional[str] = mapped_column(String(500), nullable=True)

    # Relationships
    rooms: list["Room"] = relationship(back_populates="school", cascade="all, delete-orphan")
    teachers: list["Teacher"] = relationship(back_populates="school", cascade="all, delete-orphan")
    classes: list["Class"] = relationship(back_populates="school", cascade="all, delete-orphan")
    subjects: list["Subject"] = relationship(back_populates="school", cascade="all, delete-orphan")
