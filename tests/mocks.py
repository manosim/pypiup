import unittest
import httpretty


class TestMockedRequests(unittest.TestCase):

    def setUp(self):
        super(TestMockedRequests, self).setUp()
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/Django/json", status=200, body='{"info": {"version": "1.9"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/djangorestframework/json", status=200, body='{"info": {"version": "3.3.2"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/drfdocs/json", status=200, body='{"info": {"version": "0.0.5"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/testing-errors-abc/json", status=404, body='Not found.', content_type="text/json")

    def tearDownModule(self):
        super(TestMockedRequests, self).tearDownModule()
        httpretty.disable()
        httpretty.reset()


class TestMockedDemoRequests(unittest.TestCase):

    def setUp(self):
        super(TestMockedDemoRequests, self).setUp()
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/Django/json", status=200, body='{"info": {"version": "1.9"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/djangorestframework/json", status=200, body='{"info": {"version": "3.3.1"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/django-crispy-forms/json", status=200, body='{"info": {"version": "1.5.0"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/django-push-notifications/json", status=200, body='{"info": {"version": "1.3.1"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/drfdocs/json", status=200, body='{"info": {"version": "0.0.5"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/apscheduler/json", status=200, body='{"info": {"version": "3.0.3"}}', content_type="text/json")
        httpretty.register_uri(httpretty.GET, "https://pypi.python.org/pypi/testing-errors-abc/json", status=404, body='Not found.', content_type="text/json")

    def tearDownModule(self):
        super(TestMockedDemoRequests, self).tearDownModule()
        httpretty.disable()
        httpretty.reset()
