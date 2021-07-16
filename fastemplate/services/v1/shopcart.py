from fastapi import APIRouter

from fastemplate import logger
from fastemplate.module import cart
from typing import Optional

from fastemplate.objects.cart import CartItem, CartItemsList


router = APIRouter()


@router.put('/create/{cart_id}')
def create(cart_id: str):
    """
    Creates a cart.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/create/{cart_id}')
    return cart.create_cart(id=cart_id)


@router.delete('/erase/{cart_id}')
def erase(cart_id: str):
    """
    Erases a cart.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/erase/{cart_id}')
    return cart.erase_cart(id=cart_id)


@router.post('/add_item/{cart_id}')
def add_item(cart_id: str, item: CartItem):
    """
    Endpoint. Add item to cart.

    :param str cart_id: cart id
    :param CartItem item: pair of name and price
    :return: dict
    """
    logger.info(f'Request@/add_item/{cart_id}')
    return cart.add_item(id=cart_id, item=item)


@router.post('/add_list/{cart_id}')
def add_list(cart_id: str, items: CartItemsList):
    """
    Endpoint. Add items list to cart.

    :param str cart_id: cart id
    :param CartItemsList items: items list
    :return dict: dict
    """
    logger.info(f'Request@/add_list/{cart_id}')
    return cart.add_list(id=cart_id, items=items)

@router.post('/edit_item/{cart_id}')
def edit_item(cart_id: str, item: CartItem):
    """
    Removes an item from the cart.
    
    If price is set to zero (`0`), item is removed from cart.

    :param str cart_id: cart id
    :param CartItem item: pair of name and price
    :return: dict
    """
    logger.info(f'Request@/edit_item/{cart_id}')
    return cart.edit_item(id=cart_id, item=item)

@router.delete('/delete/{cart_id}/{item_name}')
def remove_item(cart_id: str, item_name: str):
    """
    Endpoint. Removens an item from a cart.
    
    :param str cart_id: cart id
    :param str item_name: item name
    :return: dict
    """
    logger.info(f'Request@/delete/{cart_id}/{item_name}')
    return cart.remove_item(id=cart_id, item_name=item_name)

@router.get('/item/{cart_id}/price/{item_name}')
def item_price(cart_id: str, item_name: str):
    """
    Endpoint. Returns an item price.
    
    :param str cart_id: cart id
    :param str item_name: item name
    :return: dict
    """
    logger.info(f'Request@/item/{cart_id}/price/{item_name}')
    return cart.item_price(id=cart_id, item_name=item_name)

@router.get('/list_items/{cart_id}')
def list_items(cart_id: str):
    """
    Endpoint. Retrieves the cart's items and prices.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/list_items/{cart_id}')
    return cart.list_cart(id=cart_id)

@router.get('/list_some_items/{cart_id}')
def list_some_items(cart_id: str, start: int, stop: Optional[int] = None):
    """
    Endpoint. List a items from the cart, based on a range.

    :param str cart_id: cart id
    :param int start: first index to iterate
    :param Optional[int] stop: last index to iterate
    :return: dict
    """
    logger.info(f'Request@/list_some_items/{cart_id}')
    return cart.list_some_items(id=cart_id, start=start, stop=stop)


@router.get('/cost/{cart_id}')
def cost(cart_id: str):
    """
    Endpoint. Returns the total cost of the cart.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/cost/{cart_id}')
    return cart.total_cost(id=cart_id)


@router.post('/checkout/{cart_id}')
def checkout(cart_id: str):
    """
    Endpoint. Return a summary and erases the cart.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/checkout/{cart_id}')
    return cart.checkout(id=cart_id)

@router.get('/show_carts')
def cost():
    """
    Endpoint. Returns all carts.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/show_carts')
    return cart.show_carts()
