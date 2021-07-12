import unittest

from fastemplate import __api_version__

from tests import client_app


class TestPingRoot(unittest.TestCase):
    response = client_app.get(url='/')

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        chaves_esperadas = {"APPLICATION", "VERSION", "API VERSION", "DOCUMENTATION", "@TIMESTAMP"}
        self.assertEqual(sorted(list(self.response.json().keys())), sorted(list(chaves_esperadas)))

    def test_api_version(self):
        self.assertEqual(self.response.json().get('API VERSION'), __api_version__)


class TestPingMetrics(unittest.TestCase):
    response = client_app.get(url='/metrics')

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        chaves_esperadas = {"alive", "@timestamp", "no. of requests"}
        self.assertEqual(sorted(list(self.response.json().keys())), sorted(list(chaves_esperadas)))
