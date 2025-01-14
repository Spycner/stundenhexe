"""Common model types and annotations."""

from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import mapped_column

# Common field types
name_type = Annotated[str, mapped_column(String(100), nullable=False)]
