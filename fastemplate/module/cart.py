
from fastemplate import logger
from fastemplate.objects.cart import CartItem, CartItemsList
from fastemplate.exceptions.cart import CartIdAlreadyExistsException, CartIdNotFoundException, ItemNotFoundException, \
    MismatchedLenghtException, ItemAlreadyAddedException

_CART = {}
#FIXME: REMOVE
_CART['x'] = {"potato": 1.25, "orange": 2, "tomato": 0.8}


def create_cart(id: str):
    """
    Creates a cart.

    :param str id: cart id
    :return: dict
    """
    if id in _CART:
        raise CartIdAlreadyExistsException(status_code=503,
            message='Cart #{id} already in use. Checkout or delete it first.')
    else:
        _CART[id] = {}
        return {'message': f'created cart #{id}.'}


# TODO: decorator
def erase_cart(id: str):
    """
    Erases a cart.

    :param str id: cart id
    :return: dict
    """
    del _CART[id]
    return {'message': f'Successfully erased cart #{id}.'}


# TODO: decorator
def add_item(id: str, item=CartItem):
    """
    Add item to cart.

    :param str id: cart id
    :param CartItem item: pair of name and price
    :return: dict
    """
    if item.name in _CART[id]:
        raise ItemAlreadyAddedException(status_code=422,
            message=f'Item already added: {item.name} - {_CART[id][item.name]}.')
    else:
        _CART[id][item.name] = item.price
    return {'cart': id, 'item': item.name, 'price': item.price}


# TODO: decorator
def add_list(id: str, items: CartItemsList):
    """
    Add items list to cart.

    :param str id: cart id
    :param CartItemsList items: items list
    :return dict: dict
    """
    repeated = []
    if len(items.names) != len(items.prices):
        raise MismatchedLenghtException(status_code=422,
            message=f'Found {len(items.names)} items and {len(items.prices)} prices.')
    for i, p in dict(zip(items.names, items.prices)).items():
        if i in _CART[id]:
            repeated.append(i)
        else:
            _CART[id][i] = p
    if repeated != []:
        raise ItemAlreadyAddedException(status_code=422,
            message=f'Repeated items: {", ".join(repeated)}.')
    else:        
        return {'cart': id, 'message': f'added {len(items.names)} items', 'cost': sum(items.prices)}


# TODO: decorator
def edit_item(id: str, item: CartItem):
    """
    Removes an item from the cart.
    
    If price is set to zero (0), item is removed from cart.

    :param str id: cart id
    :param CartItem item: pair of name and price
    :return: dict
    """
    if item.price == 0:
        try:
            del _CART[id][item.name]
            return {'cart': id, 'message': f'removed {item.name}.'}
        except KeyError:
            raise ItemNotFoundException(status_code=404, message=f'Item not found {item.name}.')
    else:
        _CART[id][item.name] = item.price
        return {'cart': id, 'message': f'adjusted {item.name} to {item.price}.'}


def remove_item(id: str, item_name: str):
    """
    """
    try:
        del _CART[id][item_name]
        return {'cart': id, 'message': f'removed {item_name}.'}
    except KeyError:
        raise ItemNotFoundException(status_code=404, message=f'Item not found {item_name}.')


# TODO: decorator
def list_cart(id: str):
    """
    Retrieves the cart's items and prices.

    :param str id: cart id
    :return: dict
    """
    return _CART[id]


# TODO: decorator
def list_some_items(id: str, start: int, stop: int):
    """
    List a items from the cart, based on a range.

    :param str id: cart id
    :param int start: first index to iterate
    :param int stop: last index to iterate
    :return: dict
    """
    return {i:_CART[id][i] for i in list(_CART[id].keys())[start:stop]}


def item_price(id: str, item_name: str):
    """
    """
    return {item_name: _CART[id][item_name]}


# TODO: decorator
def total_cost(id: str):
    """
    Returns the total cost of the cart.

    :param str id: cart id
    :return: dict
    """
    s = []
    for k, v in _CART[id].items():
        s.append(v)
    return {id: sum(s)}


# TODO: decorator
def checkout(id: str):
    """
    Return a summary and erases the cart.

    :param str id: cart id
    :return: dict
    """
    msg = {id: list_cart(id=id), 'cost': total_cost(id=id)[id]}
    erase_cart(id=id)
    return msg
