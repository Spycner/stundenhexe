"""Base model with common fields for all models."""

from datetime import datetime
from typing import Annotated
from uuid import UUID, uuid4

from sqlalchemy import text
from sqlalchemy.orm import mapped_column

from studenhexe.db.base import Base

pk_type = Annotated[UUID, mapped_column(primary_key=True, default=uuid4)]
created_at_type = Annotated[
    datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"), nullable=False)
]
updated_at_type = Annotated[
    datetime,
    mapped_column(
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        nullable=False,
    ),
]


class BaseModel(Base):
    """Base model with common fields."""

    __abstract__ = True

    id: pk_type
    created_at: created_at_type
    updated_at: updated_at_type
