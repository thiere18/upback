from re import S
from sqlalchemy import Boolean, Column, Integer, String

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    restricted_areas = Column(String)
    permitted_areas = Column(String)
    restricted_sources = Column(String)
    permitted_sources = Column(String)
    restricted_tags = Column(String)
    permitted_tags = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # is_superuser = Column(Boolean, default=False)
    role = Column(String,nullable=False, default="normal") 
