from fastapi import APIRouter

from fastemplate.services.v1 import shopcart, fridge

v1 = APIRouter()

v1.include_router(fridge.router, prefix='/fridge', tags=['fridge'])
v1.include_router(shopcart.router, prefix='/shopcart', tags=['shopcart'])
