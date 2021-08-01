from typing import List, Set
from pydantic import BaseModel, Field


class CartItem(BaseModel):
    """
    Schema to represent an item when receiving a request.
    """
    name: str = Field(description='Item name', default='berries')
    price: float = Field(description='Item price', default=1.25)


class ItemPack(CartItem):
    """
    Schema to represent a pack item when receiving a request.
    Since it extends `CartItem`, it will, basically, be the same
    as a CartItem with the added `qnt` field.
    """
    qnt: int = Field(description='Quantity', default=1)


class CartItemsList(BaseModel):
    """
    Schema to represent a list of items when receiving a request.
    """
    names: Set[str] = Field(
        description='List of items names',
        default=['potato', 'orange', 'tomato'])
    prices: List[float] = Field(
        description='List of items prices',
        default=[1.25, 2, 0.8])
