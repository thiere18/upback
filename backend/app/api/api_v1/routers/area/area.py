
from typing import Any, List
from fastapi import  APIRouter
area_router=r = APIRouter()

@r.get('/custom-areas')
def get_custom_areas():
    {"msg": "List of custom areas"}
    
@r.get('/custom-areas/{mrgid1}/{mrgid2}')
def get_custom_areas_params(mrgid1:int, mrgid2:int):
    return {"Area shapefile":mrgid1, "Areas geohashes":mrgid2}
    

@r.get('/geo-areas/{mrgid1},{mrgid2}')
def get_user(mrgid1: int, mrgid2: int)->Any:
    return {"Area shapefile":mrgid1, "Areas geohashes":mrgid2}

@r.put('/custom-areas/put')
def get_all_area_params()->Any:
    pass
 
