#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal


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
            # restricted_areas="200 34 3",
            # permitted_areas="34 44",
            # restricted_sources=" 34 455 677",
            # permitted_sources="3456 7788 ",
            # restricted_tags="43",
            # permitted_tags="444 445 5"
        ),
    )


if __name__ == "__main__":
    print("Creating superuser admin@fan.com with admin as username")
    init()
    print("Superuser created")
