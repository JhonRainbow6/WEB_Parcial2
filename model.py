from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime, timezone


class Dog(SQLModel, table = True):
    __tablename__ = "dogs"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

"""class Sticker(SQLModel, table = True):
    __tablename__ = "stickers"

    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Book(SQLModel, table = True):
    __tablename__ = "books"

    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))"""