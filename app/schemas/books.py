from typing import Optional

from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=1, description="Book title is required")
    author: str
    year_published: Optional[int]
    is_available: bool


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year_published: Optional[int] = None
    is_available: Optional[bool] = None


class BookOutput(BaseModel):
    id: int
    title: str
    author: str
    year_published: Optional[int]
    is_available: bool

    class Config:
        from_attributes = True