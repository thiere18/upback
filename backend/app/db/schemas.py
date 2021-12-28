import json
from pydantic import BaseModel
import typing as t

from pydantic.types import Json
from sqlalchemy.dialects.postgresql.json import JSONB

# f={
#     "areas":t.List[int],
#     "sources":t.List[int],
#     "tags":t.List[str]
    
# }

class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool = True
    # is_superuser: bool = False
    first_name: str = None
    last_name: str = None
    role: t.Optional[str] = "user"
    permitted: t.Dict[t.Any, t.Any] 
    restricted: t.Dict[t.Any, t.Any]
    # class Config:
    #     orm_mode = True



class UserOut(UserBase):
    pass


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "normal"
