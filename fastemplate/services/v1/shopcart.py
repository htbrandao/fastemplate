from typing import Optional

from fastapi import APIRouter, UploadFile, File, Depends, Header

from fastemplate import logger
from fastemplate.module import cart
from fastemplate.objects.cart import CartItem, CartItemsList
from fastemplate.exceptions.cart import InvalidCredentialsException


router = APIRouter()


@router.post('/create/{cart_id}', status_code=201)
def create(cart_id: str):
    """
    Creates a cart.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/create/{cart_id}')
    return cart.create_cart(id=cart_id)


@router.post("/upload_shoplist/{cart_id}", status_code=201)
def upload_shoplist(cart_id:str, file: UploadFile = File(...)):
    """
    Uploads a `.csv` file to **create** a cart.

    :param str id: cart id
    :param File file: file containing item name and price
    :return: dict
    """
    logger.info(f'Request@/upload_shoplist/{cart_id}')
    return cart.upload_shoplist(id=cart_id, file=file)


@router.delete('/erase/{cart_id}')
def erase(cart_id: str):
    """
    Erases a cart.

    :param str cart_id: cart id
    :return: dict
    """
    logger.info(f'Request@/erase/{cart_id}')
    return cart.erase_cart(id=cart_id)


@router.put('/add_item/{cart_id}')
def add_item(cart_id: str, item: CartItem):
    """
    Endpoint. Add item to cart.

    :param str cart_id: cart id
    :param CartItem item: pair of name and price
    :return: dict
    """
    logger.info(f'Request@/add_item/{cart_id}')
    return cart.add_item(id=cart_id, item=item)


@router.put('/add_list/{cart_id}')
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


def common_parameters(cart_id: str, item_name: str):
    """
    # TODO: docstring
    """
    return {"cart_id": cart_id, "item_name": item_name}


@router.delete('/remove_item')
def remove_item(commons: dict = Depends(common_parameters)):
    """
    # TODO: docstring
    """
    logger.info(f'Request@/remove_item/{commons["cart_id"]}/{commons["item_name"]}')
    return cart.remove_item(id=commons['cart_id'], item_name=commons['item_name'])


@router.get('/item_price')
def item_price(commons=Depends(common_parameters)):
    """
    # TODO: docstring
    """
    logger.info(f'Request@/item_price/{commons["cart_id"]}/{commons["item_name"]}')
    return cart.item_price(id=commons['cart_id'], item_name=commons['item_name'])


@router.get('/list_items')
def list_items(cart_id: Optional[str] = None):
    """
    # TODO: docstring
    """
    if cart_id:
        logger.info(f'Request@/list_items/{cart_id}')
        return cart.list_cart(id=cart_id)
    else:
        logger.info(f'Request@/list_items')
        return cart.show_carts()


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


def verify_token(x_token: str = Header(...)):
    real_token = "you-will-never-guess"
    if x_token != real_token:
        raise InvalidCredentialsException(message="X-Token header invalid")


def verify_key(x_key: str = Header(...)):
    real_key = "i-double-dare-you"
    if x_key != real_key:
        raise InvalidCredentialsException(message="X-Key header invalid")


@router.delete('/nuke', dependencies=[Depends(verify_token), Depends(verify_key)])
def nuke():
    """
    # TODO: docstring
    """
    logger.info(f'Request@/nuke')
    return cart.nuke()

