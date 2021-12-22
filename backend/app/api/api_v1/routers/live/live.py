
from typing import Any, List
from fastapi import  APIRouter
live_router=r = APIRouter()

@r.get('/live-ships{update_id}')
def get_me(update_id: int):
    return {"msg": update_id}



