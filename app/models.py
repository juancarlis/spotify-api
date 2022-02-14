# Python
from datetime import date

# Pydantic
from pydantic import BaseModel
from pydantic import Field


# Models

class Album(BaseModel):
    name: str = Field(...)
    release: date
    tracks_qty: int = Field(...)
    cover: dict = Field()
