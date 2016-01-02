import unittest
from click.testing import CliRunner
from pypi_uptodate.cli import cli
from tests.mocks import TestMockedRequests


class TestRequirementsMockedRequests(TestMockedRequests):

    def setUp(self):
        super(TestRequirementsMockedRequests, self).setUp()

    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['-r', 'requirements/requirements-tests.txt'])

        self.assertEqual(result.exit_code, 0)

        # Django
        self.assertIn("Needs update, From 1.7.1 to 1.9.0.", result.output)

        # djangorestframework
        self.assertIn("Up to date, 3.3.2.", result.output)

        # drfdocs
        self.assertIn("Up to date, 0.0.5.", result.output)

        self.assertIn("Total Requirements: 5", result.output)
        self.assertIn("Up to date: 2", result.output)
        self.assertIn("Update available: 1", result.output)
        self.assertIn("Invalid Semver: 0", result.output)
        self.assertIn("Non PyPI Requirements: 2", result.output)


class TestRequirementsFileNotFound(unittest.TestCase):

    def test_cli_file_not_found(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['-r', 'requirements-fake.txt'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Could not find requirements-fake.txt. No such file or directory.", result.output)

if __name__ == '__main__':
    unittest.main()
