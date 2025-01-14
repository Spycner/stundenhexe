"""Room model definition."""

from enum import Enum
from typing import Annotated, Optional
from uuid import UUID

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship

from studenhexe.models.base import BaseModel
from studenhexe.models.types import name_type


class RoomType(str, Enum):
    """Room type enumeration."""

    CLASSROOM = "CLASSROOM"
    LAB = "LAB"
    GYM = "GYM"
    LIBRARY = "LIBRARY"
    CAFETERIA = "CAFETERIA"
    AUDITORIUM = "AUDITORIUM"
    OTHER = "OTHER"


class Room(BaseModel):
    """Room model representing a physical space in a school."""

    __tablename__ = "rooms"

    name: name_type
    capacity: Annotated[int, mapped_column(nullable=False)]
    type: Annotated[RoomType, mapped_column(SQLEnum(RoomType), nullable=False)] = mapped_column(
        default=RoomType.CLASSROOM
    )
    features: Annotated[list[str], mapped_column(nullable=True)] = mapped_column(
        default_factory=list
    )
    description: Optional[str] = mapped_column(String(500), nullable=True)

    # Foreign keys
    school_id: Annotated[UUID, mapped_column(ForeignKey("schools.id", ondelete="CASCADE"))]

    # Relationships
    school: "School" = relationship(back_populates="rooms")
    schedules: list["Schedule"] = relationship(back_populates="room", cascade="all, delete-orphan")
