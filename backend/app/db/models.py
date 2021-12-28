from re import S
from sqlalchemy import Boolean, Column, Integer, String,JSON
# from sqlalchemy.sql.sqltypes import JSON
from sqlalchemy.dialects.postgresql import JSONB

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    permitted = Column(JSONB)
    restricted = Column(JSONB)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # is_superuser = Column(Boolean, default=False)
    role = Column(String,nullable=False, default="normal") 
