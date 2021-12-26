from pydantic import BaseModel
import typing as t


class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool = True
    # is_superuser: bool = False
    first_name: str = None
    last_name: str = None
    role: t.Optional[str] = "user"
    restricted_areas: str= None
    permitted_areas: str= None
    restricted_sources: str= None
    permitted_sources: str= None
    restricted_tags: str= None
    permitted_tags: str= None
    



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
