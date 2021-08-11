import unittest

from fastemplate import __api_version__, __version__

from tests import client_app


class TestPingRoot(unittest.TestCase):
    response = client_app.get(url='/')

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'APPLICATION', 'VERSION', 'API VERSION', 'DOCUMENTATION', '@TIMESTAMP'}
        self.assertEqual(sorted(list(self.response.json().keys())), sorted(list(expected_keys)))

    def test_api_version(self):
        self.assertEqual(self.response.json().get('API VERSION'), __api_version__)

    def test_application_version(self):
        self.assertEqual(self.response.json().get('VERSION'), __version__)


class TestPingRedirectSource(unittest.TestCase):
    response = client_app.get(url='/metrics')

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)


class TestPingMetrics(unittest.TestCase):
    response = client_app.get(url='/metrics')

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'alive', '@timestamp', 'no. of requests'}
        self.assertEqual(sorted(list(self.response.json().keys())), sorted(list(expected_keys)))

    def test_response_content_values_types(self):
        self.assertIsInstance(self.response.json().get('alive'), bool)
        self.assertIsInstance(self.response.json().get('@timestamp'), str)
        self.assertIsInstance(self.response.json().get('no. of requests'), int)


class TestPingExploreRequest(unittest.TestCase):
    response = client_app.get(url='/explore_request')

    def test_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_type(self):
        self.assertIsInstance(self.response.json(), dict)

    def test_response_content(self):
        expected_keys = {'client', 'cookies', 'base_url', 'headers', 'method', 'query_params', 'path_params'}
        self.assertEqual(sorted(list(self.response.json().keys())), sorted(list(expected_keys)))

    def test_response_content_values_types(self):
        self.assertIsInstance(self.response.json().get('client'), list)
        self.assertIsInstance(self.response.json().get('client')[0], str)
        self.assertIsInstance(self.response.json().get('client')[1], int)
        self.assertIsInstance(self.response.json().get('cookies'), dict)
        self.assertIsInstance(self.response.json().get('base_url'), dict)
        self.assertIsInstance(self.response.json().get('base_url').get('_url'), str)
        self.assertIsInstance(self.response.json().get('headers'), dict)
        self.assertIsInstance(self.response.json().get('method'), str)
        self.assertIsInstance(self.response.json().get('query_params'), dict)
        self.assertIsInstance(self.response.json().get('path_params'), dict)

    def test_response_content_value_header(self):
        expected_keys = {'host', 'user-agent', 'accept', 'accept-encoding', 'connection'}
        self.assertEqual(sorted(list(self.response.json().get('headers').keys())), sorted(list(expected_keys)))
