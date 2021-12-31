#!/usr/bin/env python3
import asyncio 
from app.db.session import get_db
from app.db.crud import create_user ,create_role
from app.db.schemas import UserCreate,Role
from app.db.session import SessionLocal
import json

data={
                "sources": "12",
                "areas": "12",
                "tags":  "no-go"
            }
def ino() -> None:
    db = SessionLocal()
    create_role(
        db, 
        Role(
            name='admin'
        )
    )
    
def init() -> None:
    db = SessionLocal()
    create_user(
        db,
        UserCreate(
            username='admin',
            email="admin@fan.com",
            password="password",
            is_active=True,
            role_id=1,
            permitted=data,
            restricted=data
            
        ),
    )


if __name__ == "__main__":
    print("Creating superuser admin@fan.com with admin as username")
    ino()
    init()
    print("Superuser created")
