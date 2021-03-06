from fastapi import HTTPException, status,Depends
from sqlalchemy.orm import Session
import typing as t

from . import models, schemas
from app.core.security import get_password_hash


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_email(db: Session, email: str) -> schemas.UserBase:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_email_or_username(db: Session, username: str,email: str) -> schemas.UserBase:
    return db.query(models.User).filter((models.User.username == username)|(models.User.email == email)).first()


def get_users(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.UserOut]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # verify_user_email=db.query(models.User).filter(models.User.email==user.email)
    # verify_user_username=db.query(models.User).filter(models.User.username==user.username)
    # if verify_user_email is not None:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='user already exists')
    # if verify_user_username is not None:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='username already exists')

    hashed_password = get_password_hash(user.password)

    db_user = models.User(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        is_active=user.is_active,
        permitted=user.permitted,
        restricted=user.restricted,
        hashed_password=hashed_password,
        role_id=user.role_id,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return user


def edit_user(
    db: Session, user_id: int, user: schemas.UserEdit
) -> schemas.User:
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    print(update_data)
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(user.password)
        del update_data["password"]

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# role


def get_role(db: Session, role_id: int):
    role = db.query(models.Role).filter(models.Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="User not found")
    return role




def get_roles(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.RoleOut]:
    return db.query(models.Role).all()



def create_role(db: Session, role: schemas.Role):
    # verify_user_email=db.query(models.User).filter(models.User.email==user.email)
    # verify_user_username=db.query(models.User).filter(models.User.username==user.username)
    # if verify_user_email is not None:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='user already exists')
    # if verify_user_username is not None:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='username already exists')


    db_role = models.Role(
        name=role.name,

    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def edit_role(
    db: Session, role_id: int, role: schemas.RoleEdit
) -> schemas.RoleOut:
    db_role = get_role(db, role_id)
    if not db_role:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Role not found")
    update_data = role.dict(exclude_unset=True)
    print(update_data)

    for key, value in update_data.items():
        setattr(db_role, key, value)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
   
   
def delete_role(db: Session, role_id: int):
    role = get_role(db, role_id)
    if not role:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Role not found")
    db.delete(role)
    db.commit()
    return "success"


def get_role_user( role_id: int,db: Session ):
    role= db.query(models.Role).filter(models.Role.id == role_id).first()
    return role.name