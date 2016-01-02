import unittest
from pypi_uptodate.requirements import Requirements


class TestRequiments(unittest.TestCase):

    def setUp(self):
        super(TestRequiments, self).setUp()
        self.requirements = Requirements("requirements/requirements-tests.txt")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
