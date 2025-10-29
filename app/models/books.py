
from sqlalchemy import Column, Integer, String, Boolean

from .base import BaseModel

class Book(BaseModel):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(String)
    is_available = Column(Boolean, nullable=False, default=True)

    def __str__(self):
        return self.title
