#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal
import json

data={
                "sources": "12",
                "areas": "12",
                "tags":  "no-go"
            }
def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            username='admin',
            email="admin@fan.com",
            password="password",
            is_active=True,
            role="admin",
            permitted=data,
            restricted=data
            
        ),
    )


if __name__ == "__main__":
    print("Creating superuser admin@fan.com with admin as username")
    init()
    print("Superuser created")
