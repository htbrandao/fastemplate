import unittest

from fastemplate import __api_version__

from tests import client_app

TEST_CART_ID = 'myLittleCart'
MOCK_CART_ID = 'breakfast'
NOISE = '!@'


class TestShopCartCreate(unittest.TestCase):
    response = client_app.post(url=f'/{__api_version__}/shopcart/create/{TEST_CART_ID}')

    def test_return_201(self):
        self.assertEqual(self.response.status_code, 201)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'message'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('message'), f'created cart #{TEST_CART_ID}.')


class TestShopCartCreateExisting(unittest.TestCase):
    response = client_app.post(url=f'/{__api_version__}/shopcart/create/{MOCK_CART_ID}')

    def test_return_503(self):
        self.assertEqual(self.response.status_code, 503)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'message', 'status', 'exception'}
        self.assertEqual(sorted(self.response.json().keys()), sorted(expected_keys))


# FIXME: TestShopCartUploadShoplist
# class TestShopCartUploadShoplist(unittest.TestCase):
#     FILE_PATH = 'tests/unit/shoplist.csv'
#     FILE_BYTES = open(FILE_PATH, 'rb').read()
#     FILE_TEXT = open(FILE_PATH, 'r').read()
#     FILE_CART = dict([(x[0], x[1]) for x in [x.split(',') for x in FILE_TEXT.split('\n')]])
#     REQUEST_FILE = {
#         'file': (FILE_PATH.split('/')[-1], FILE_BYTES, 'text/csv'),
#     }
#     response = client_app.post(url=f'/{__api_version__}/shopcart/upload_shoplist/{NEW_CART_ID}', files=REQUEST_FILE)

#     def test_return_201(self):
#         self.assertEqual(self.response.status_code, 201)

#     def test_response_content(self):
#         expected_keys = {'filename', 'type', 'cart'}
#         self.assertEqual(sorted(self.response.json().keys()), sorted(expected_keys))
#         self.assertEqual(self.response.json().get('cart'), self.FILE_CART)


class TestShopCartErase(unittest.TestCase):
    response = client_app.delete(url=f'/{__api_version__}/shopcart/erase/{MOCK_CART_ID}')

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'message'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('message'), f'Successfully erased cart #{MOCK_CART_ID}.')


class TestShopCartEraseNonExisting(unittest.TestCase):
    response = client_app.delete(url=f'/{__api_version__}/shopcart/erase/{TEST_CART_ID+NOISE}')

    def test_return_404(self):
        self.assertEqual(self.response.status_code, 404)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'status', 'exception', 'message'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('status'), 404)
        self.assertEqual(self.response.json().get('message'), f'Cart #{TEST_CART_ID+NOISE} does not exist.')
        self.assertEqual(self.response.json().get('exception'), 'CartIdNotFoundException')


class TestShopCartAddItem(unittest.TestCase):
    data = {'name': 'berries', 'price': 1.25}
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_item/{TEST_CART_ID}', json=data)

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'cart', 'item', 'price'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('cart'), TEST_CART_ID)
        self.assertEqual(self.response.json().get('item'), self.data['name'])
        self.assertEqual(self.response.json().get('price'), self.data['price'])


class TestShopCartAddItemNonExisting(unittest.TestCase):
    data = {'name': 'berries', 'price': 1.25}
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_item/{TEST_CART_ID+NOISE}', json=data)

    def test_return_404(self):
        self.assertEqual(self.response.status_code, 404)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'status', 'message', 'exception'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('status'), 404)
        self.assertEqual(self.response.json().get('message'), f'Cart #{TEST_CART_ID+NOISE} does not exist.')
        self.assertEqual(self.response.json().get('exception'), 'CartIdNotFoundException')


class TestShopCartAddItemAgain(unittest.TestCase):
    data = {'name': 'berries', 'price': 1.25}
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_item/{TEST_CART_ID}', json=data)
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_item/{TEST_CART_ID}', json=data)

    def test_return_422(self):
        self.assertEqual(self.response.status_code, 422)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'status', 'message', 'exception'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('status'), 422)
        self.assertEqual(self.response.json().get('message'), f'Item already added: {self.data["name"]} - {self.data["price"]}.')
        self.assertEqual(self.response.json().get('exception'), 'ItemAlreadyAddedException')


class TestShopCartAddList(unittest.TestCase):
    data = {'names': ['potato', 'orange', 'tomato'],'prices': [1.25, 2, 0.8]}
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_list/{TEST_CART_ID}', json=data)

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'cart', 'message', 'cost'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('cart'), TEST_CART_ID)
        self.assertEqual(self.response.json().get('message'), f'added {len(self.data["names"])} items')
        self.assertEqual(self.response.json().get('cost'), sum(self.data['prices']))


class TestShopCartAddListNonExisting(unittest.TestCase):
    data = {'names': ['potato', 'orange', 'tomato'],'prices': [1.25, 2, 0.8]}
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_list/{TEST_CART_ID+NOISE}', json=data)

    def test_return_404(self):
        self.assertEqual(self.response.status_code, 404)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'status', 'message', 'exception'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('status'), 404)
        self.assertEqual(self.response.json().get('message'), f'Cart #{TEST_CART_ID+NOISE} does not exist.')
        self.assertEqual(self.response.json().get('exception'), 'CartIdNotFoundException')


class TestShopCartAddItemAgain(unittest.TestCase):
    data = {'names': ['orange', 'potato', 'tomato'],'prices': [1.25, 2, 0.8]}
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_list/{TEST_CART_ID}', json=data)
    response = client_app.put(url=f'/{__api_version__}/shopcart/add_list/{TEST_CART_ID}', json=data)

    def test_return_422(self):
        self.assertEqual(self.response.status_code, 422)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'status', 'message', 'exception'}
        self.assertEqual(self.response.json().keys(), expected_keys)
        self.assertEqual(self.response.json().get('status'), 422)
        self.assertEqual(self.response.json().get('exception'), 'ItemAlreadyAddedException')
    
    def test_repeated_items(self):
        response_fruits = self.response.json().get('message').replace('Repeated items: ', '').replace('.', '').split(', ')
        expected_fruits = ', '.join(self.data['names']).split(', ')
        self.assertEqual(sorted(response_fruits), sorted(expected_fruits))


# TODO: edit_item
# TODO: remove_item
# TODO: item_price
# TODO: list_items
# TODO: list_some_items
# TODO: cost
# TODO: checkout
# TODO: show_carts
# TODO: nuke 
