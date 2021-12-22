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
    permissions: str = "user"
