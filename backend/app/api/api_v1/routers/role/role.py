from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud import (
    get_roles,
    get_role,
    create_role,
    delete_role,
    edit_role,
)
from app.db.schemas import UserCreate, UserEdit, User, UserOut ,Role, RoleOut,RoleEdit
from app.core.auth import get_current_active_user, get_current_active_superuser

role_router = r = APIRouter()

@r.get(
    "/roles",
    response_model=t.List[RoleOut],
    response_model_exclude_none=True,


)
async def role_list(
    response: Response,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Get all roles
    """
    roles = get_roles(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(roles)}"
    response.headers['X-Total-Count'] = '30' 
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'

    return roles


@r.get(
    "/roles/{role_id}",
    response_model=RoleOut,
    response_model_exclude_none=True,
)
async def role_details(
    request: Request,
    role_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Get any user details
    """
    return get_role(db, role_id)
    # return encoders.jsonable_encoder(
    #     user, skip_defaults=True, exclude_none=True,
    # )


@r.post("/roles", response_model=RoleOut, response_model_exclude_none=True)
async def user_create(
    request: Request,
    role: Role,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new user
    """
    return create_role(db, role)


@r.put(
    "/roles/{role_id}", response_model=RoleOut, response_model_exclude_none=True
)
async def role_edit(
    request: Request,
    role_id: int,
    role: RoleEdit,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Update existing user
    """
    return edit_role(db, role_id, role)


@r.delete(
    "/roles/{role_id}", response_model=Role, response_model_exclude_none=True
)
async def role_delete(
    request: Request,
    role_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Delete existing user
    """
    return delete_role(db, role_id)
