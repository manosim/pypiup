import unittest
# import click
from click.testing import CliRunner
from pypi_uptodate.cli import cli


class TestRequirements(unittest.TestCase):

    # def setUp(self):
        # super(TestRequiments, self).setUp()
        # self.requirements = Requirements("requirements/requirements-tests.txt")

    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['-r', 'requirements/requirements-tests.txt'])

        # print(result)
        # print(result.output)
        # print(dir(result))

        # assert result.exit_code == 0
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Django", result.output)

    def test_cli_file_not_found(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['-r', 'requirements-fake.txt'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Could not find requirements-fake.txt. No such file or directory.", result.output)

if __name__ == '__main__':
    unittest.main()
