"""Models package."""

from studenhexe.models.base import BaseModel
from studenhexe.models.room import Room, RoomType
from studenhexe.models.school import School

__all__ = ["BaseModel", "School", "Room", "RoomType"]

# Forward references for type hints
Teacher = None
Class = None
Subject = None
Schedule = None
