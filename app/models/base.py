from sqlalchemy import Boolean, Column, DateTime, Integer, text
from sqlalchemy.sql import func

from app.database import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now(), server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), server_default=text('CURRENT_TIMESTAMP'))
    is_active = Column(Boolean, default=True)
