import functools

from fastapi import File

from fastemplate import logger
from fastemplate.module import MOCK_BASE_CART
from fastemplate.objects.cart import CartItem, CartItemsList
from fastemplate.exceptions.cart import CartIdAlreadyExistsException, CartIdNotFoundException, ItemNotFoundException, \
    MismatchedLenghtException, ItemAlreadyAddedException, UnsupportedFileExtensionException


def create_cart(cart_id: str):
    """
    Creates a cart.

    :param str cart_id: cart id
    :return: dict with message
    :rtype: dict
    :raises: CartIdAlreadyExistsException
    """
    if cart_id in MOCK_BASE_CART:
        raise CartIdAlreadyExistsException(message=f'Cart #{cart_id} already in use. Checkout or delete it first.')
    else:
        MOCK_BASE_CART[cart_id] = {}
        return {'message': f'created cart #{cart_id}.'}


def hasId(func):
    """
    Wrapper to check if cart has the given id.
    """
    @functools.wraps(func)
    def wrapper_hasId(**kwargs):
        """
        Wrapper function for `hasId`.

        :params dict kwargs: decorated function kwargs
        :return: func(**kwargs)
        :rtype: func
        :raises: CartIdNotFoundException
        """
        cart_id = {**kwargs}['id']
        if cart_id in MOCK_BASE_CART:
            return func(**kwargs)
        else:
            raise CartIdNotFoundException(message=f'Cart #{cart_id} does not exist.')
    return wrapper_hasId


def upload_shoplist(id: str, file: File):
    """
    Uploads a `.csv` file to create a cart.

    :param str id: cart id
    :param File file: file containing item name and price
    :return: dict with filename, type and cart
    :rtype: dict
    :raises: UnsupportedFileExtensionException
    """
    if '.csv' not in file.filename:
        raise UnsupportedFileExtensionException(message=f'File {file.filename} is not supported.')
    else:
        create_cart(cart_id=id)
        content_bytes = file.file.read()
        content_str = content_bytes.decode('utf-8').split('\n')
        shoplist = dict([
            [i.split(',')[0], float(i.split(',')[1])]
            for i in content_str
        ])
        MOCK_BASE_CART[id] = shoplist
        return {
            'filename': file.filename,
            'type': file.content_type,
            'cart': MOCK_BASE_CART[id]
        }


@hasId
def erase_cart(cart_id: str):
    """
    Erases a cart.

    :param str cart_id: cart id
    :return: dict with message
    :rtype: dict
    """
    del MOCK_BASE_CART[cart_id]
    return {'message': f'Successfully erased cart #{cart_id}.'}


@hasId
def add_item(cart_id: str, item=CartItem):
    """
    Add item to cart.

    :param str cart_id: cart id
    :param CartItem item: pair of name and price
    :return: dict with cart, item and price
    :rtype: dict
    :raises: ItemAlreadyAddedException
    """
    if item.name in MOCK_BASE_CART[cart_id]:
        raise ItemAlreadyAddedException(message=f'Item already added: {item.name} - {MOCK_BASE_CART[cart_id][item.name]}.')
    else:
        MOCK_BASE_CART[cart_id][item.name] = item.price
    return {'cart': cart_id, 'item': item.name, 'price': item.price}


@hasId
def add_list(cart_id: str, items: CartItemsList):
    """
    Add items list to cart.

    :param str cart_id: cart id
    :param CartItemsList items: items list
    :return: dict with cart, message and cost
    :rtype: dict
    :raises: MismatchedLenghtException, ItemAlreadyAddedException
    """
    repeated = []
    if len(items.names) != len(items.prices):
        raise MismatchedLenghtException(message=f'Found {len(items.names)} items and {len(items.prices)} prices.')
    for i, p in dict(zip(items.names, items.prices)).items():
        if i in MOCK_BASE_CART[cart_id]:
            repeated.append(i)
        else:
            MOCK_BASE_CART[cart_id][i] = p
    if repeated != []:
        raise ItemAlreadyAddedException(
            message=f'Repeated items: {", ".join(repeated)}.')
    else:
        return {'cart': cart_id, 'message': f'added {len(items.names)} items', 'cost': sum(items.prices)}


@hasId
def edit_item(id: str, item: CartItem):
    """
    Removes an item from the cart.

    If price is set to zero (0), item is removed from cart.

    :param str id: cart id
    :param CartItem item: pair of name and price
    :return: dict with cart and message
    :rtype: dict
    :raises: ItemNotFoundException
    """
    if item.price == 0:
        try:
            del MOCK_BASE_CART[id][item.name]
            return {'cart': id, 'message': f'removed {item.name}.'}
        except KeyError:
            raise ItemNotFoundException(message=f'Item not found {item.name}.')
    else:
        MOCK_BASE_CART[id][item.name] = item.price
        return {'cart': id, 'message': f'adjusted {item.name} to {item.price}.'}


@hasId
def remove_item(cart_id: str, item_name: str):
    """
    Removes an item from cart.

    :param str cart_id: cart id
    :param str item_name: item name
    :return: dict with cart and message
    :rtype: dict
    :raises: ItemNotFoundException
    """
    try:
        del MOCK_BASE_CART[cart_id][item_name]
        return {'cart': cart_id, 'message': f'removed {item_name}.'}
    except KeyError:
        raise ItemNotFoundException(message=f'Item not found {item_name}.')


@hasId
def list_cart(cart_id: str):
    """
    Retrieves the cart's items and prices.

    :param str cart_id: cart id
    :return: dict with the cart items
    :rtype: dict
    """
    return MOCK_BASE_CART[cart_id]


@hasId
def list_some_items(cart_id: str, start: int, stop: int):
    """
    List a items from the cart, based on a range.

    :param str cart_id: cart id
    :param int start: first index to iterate
    :param int stop: last index to iterate
    :return: dict with items
    :rtype: dict
    """
    return {i:MOCK_BASE_CART[cart_id][i] for i in list(MOCK_BASE_CART[cart_id].keys())[start:stop]}


@hasId
def item_price(id: str, item_name: str):
    """
    Returns the price from an item inside a cart.

    :param str id: cart id
    :param str item_name: item name
    :return: dict with item name and price
    :rtype: dict
    """
    return {item_name: MOCK_BASE_CART[id][item_name]}


@hasId
def total_cost(cart_id: str):
    """
    Returns the total cost of the cart.

    :param str cart_id: cart id
    :return: dict with cart id and total cost
    :rtype: dict
    """
    s = []
    for v in MOCK_BASE_CART[cart_id].values():
        s.append(v)
    return {cart_id: sum(s)}


@hasId
def checkout(cart_id: str):
    """
    Return a summary and erases the cart.

    :param str cart_id: cart id
    :return: dict with id and cost
    :rtype: dict
    """
    msg = {cart_id: list_cart(cart_id=cart_id), 'cost': total_cost(cart_id=cart_id)[cart_id]}
    erase_cart(cart_id=cart_id)
    return msg


def show_carts():
    """
    Returns all carts in their current state.

    :return: dict with all carts
    :rtype: dict
    """
    return MOCK_BASE_CART


def nuke():
    """
    Erases all carts.

    :return: dict with message and carts
    :rtype: dict
    """
    MOCK_BASE_CART.clear()
    return {'message': 'all carts were obliterated', 'carts': MOCK_BASE_CART}
