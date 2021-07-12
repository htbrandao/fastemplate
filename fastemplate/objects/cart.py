from typing import List, Set
from pydantic import BaseModel, Field


class CartItem(BaseModel):
    """
    Schema to represent an item when receiving a request.
    """
    name: str = Field(description='Item name', default='berries')
    price: float = Field(description='Item price', default=1.25)


class CartItemsList(BaseModel):
    """
    Schema to represent a list of items when receiving a request.
    """
    names: Set[str] = Field(description='List of items names', default=['potato', 'orange', 'tomato'])
    prices: List[float] = Field(description='List of items prices', default=[1.25, 2, 0.8])
