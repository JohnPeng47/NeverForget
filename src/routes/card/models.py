from sqlmodel import SQLModel, Field
from typing import Optional

# Example model
class Card(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    