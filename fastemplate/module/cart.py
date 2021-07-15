import functools

from fastemplate.module import BASE_CART
from fastemplate.objects.cart import CartItem, CartItemsList
from fastemplate.exceptions.cart import CartIdAlreadyExistsException, CartIdNotFoundException, ItemNotFoundException, \
    MismatchedLenghtException, ItemAlreadyAddedException

#FIXME: REMOVE
BASE_CART['x'] = {"potato": 1.25, "orange": 2, "tomato": 0.8}

def create_cart(id: str):
    """
    Creates a cart.

    :param str id: cart id
    :return: dict
    """
    if id in BASE_CART:
        raise CartIdAlreadyExistsException(message=f'Cart #{id} already in use. Checkout or delete it first.')
    else:
        BASE_CART[id] = {}
        return {'message': f'created cart #{id}.'}

def hasId(func):
    """
    Wrapper to check if cart has the given id.
    """
    @functools.wraps(func)
    def wrapper_hasId(**kwargs):
        """
        Wrapper function for `hasId`.
        """
        cart_id = {**kwargs}['id']
        if cart_id in BASE_CART:
            return func(**kwargs)
        else:
            raise CartIdNotFoundException(message=f'Cart #{cart_id} does not exist.')
    return wrapper_hasId

@hasId
def erase_cart(id: str):
    """
    Erases a cart.

    :param str id: cart id
    :return: dict
    """
    del BASE_CART[id]
    return {'message': f'Successfully erased cart #{id}.'}

@hasId
def add_item(id: str, item=CartItem):
    """
    Add item to cart.

    :param str id: cart id
    :param CartItem item: pair of name and price
    :return: dict
    """
    if item.name in BASE_CART[id]:
        raise ItemAlreadyAddedException(message=f'Item already added: {item.name} - {BASE_CART[id][item.name]}.')
    else:
        BASE_CART[id][item.name] = item.price
    return {'cart': id, 'item': item.name, 'price': item.price}

@hasId
def add_list(id: str, items: CartItemsList):
    """
    Add items list to cart.

    :param str id: cart id
    :param CartItemsList items: items list
    :return dict: dict
    """
    repeated = []
    if len(items.names) != len(items.prices):
        raise MismatchedLenghtException(message=f'Found {len(items.names)} items and {len(items.prices)} prices.')
    for i, p in dict(zip(items.names, items.prices)).items():
        if i in BASE_CART[id]:
            repeated.append(i)
        else:
            BASE_CART[id][i] = p
    if repeated != []:
        raise ItemAlreadyAddedException(
            message=f'Repeated items: {", ".join(repeated)}.')
    else:        
        return {'cart': id, 'message': f'added {len(items.names)} items', 'cost': sum(items.prices)}

@hasId
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
            del BASE_CART[id][item.name]
            return {'cart': id, 'message': f'removed {item.name}.'}
        except KeyError:
            raise ItemNotFoundException(message=f'Item not found {item.name}.')
    else:
        BASE_CART[id][item.name] = item.price
        return {'cart': id, 'message': f'adjusted {item.name} to {item.price}.'}

@hasId
def remove_item(id: str, item_name: str):
    """
    Removes an item from cart.

    :param str id: cart id
    :return: dict
    """
    try:
        del BASE_CART[id][item_name]
        return {'cart': id, 'message': f'removed {item_name}.'}
    except KeyError:
        raise ItemNotFoundException(message=f'Item not found {item_name}.')

@hasId
def list_cart(id: str):
    """
    Retrieves the cart's items and prices.

    :param str id: cart id
    :return: dict
    """
    return BASE_CART[id]

@hasId
def list_some_items(id: str, start: int, stop: int):
    """
    List a items from the cart, based on a range.

    :param str id: cart id
    :param int start: first index to iterate
    :param int stop: last index to iterate
    :return: dict
    """
    return {i:BASE_CART[id][i] for i in list(BASE_CART[id].keys())[start:stop]}

@hasId
def item_price(id: str, item_name: str):
    """
    Returns the price from an item inside a cart.
    
    :param str id: cart id
    :return: dict
    """
    return {item_name: BASE_CART[id][item_name]}

@hasId
def total_cost(id: str):
    """
    Returns the total cost of the cart.

    :param str id: cart id
    :return: dict
    """
    s = []
    for k, v in BASE_CART[id].items():
        s.append(v)
    return {id: sum(s)}

@hasId
def checkout(id: str):
    """
    Return a summary and erases the cart.

    :param str id: cart id
    :return: dict
    """
    msg = {id: list_cart(id=id), 'cost': total_cost(id=id)[id]}
    erase_cart(id=id)
    return msg

def show_carts():
    """
    Returns all carts in their current state.

    :return: dict
    """
    return BASE_CART
