import unittest

from fastemplate import __api_version__

from tests import client_app


# class TestWhois(unittest.TestCase):
#     response = client_app.get(url=f'/{__api_version__}/login/whois')

#     def test_return_201(self):
#         self.assertEqual(self.response.status_code, 201)

#     def test_response_type(self):
#         self.assertIsInstance(self.response.json(), dict)

#     def test_response_content(self):
#         expected_keys = {}
#         self.assertEqual(self.response.json().keys(), expected_keys)


# class TestFridgeBuyAllTuna(unittest.TestCase):
#     response = client_app.post(url=f'/{__api_version__}/fridge/BUY_ALL_TUNA_THERE_IS')

#     def test_return_201(self):
#         self.assertEqual(self.response.status_code, 201)

#     def test_response_type(self):
#         self.assertIsInstance(self.response.json(), dict)

#     def test_response_content(self):
#         expected_keys = {}
#         self.assertEqual(self.response.json().keys(), expected_keys)
