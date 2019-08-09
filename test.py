"""Unit tests"""


import checksum
import click.testing
import unittest


class TestChecksum(unittest.TestCase):
    def test_valid_checksum(self):
        self.assertEqual(
            checksum.checksum(filename="test_file.txt"),
            "1296b08a46570840ca4fbe5d3a09d2ec35181581484a1b52b826b070d7054fd1",
        )

    def test_invalid_checksum(self):
        self.assertNotEqual(
            checksum.checksum(filename="test_file.txt"),
            "1296b08a46570840ca4fbe5d3a09d2ec35181581484a1b52b826b070d7054fd10",
        )


class TestChecksumCli(unittest.TestCase):
    def test_valid_calculation(self):
        cli_runner = click.testing.CliRunner()
        result = cli_runner.invoke(checksum.cli, args=["test_file.txt"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(
            result.output,
            "1296b08a46570840ca4fbe5d3a09d2ec35181581484a1b52b826b070d7054fd1\n",
        )

    def test_invalid_calculation(self):
        cli_runner = click.testing.CliRunner()
        result = cli_runner.invoke(checksum.cli, args=["test_file.txt"])
        self.assertEqual(result.exit_code, 0)
        self.assertNotEqual(
            result.output,
            "1296b08a46570840ca4fbe5d3a09d2ec35181581484a1b52b826b070d7054fd10\n",
        )

    def test_valid_expected(self):
        cli_runner = click.testing.CliRunner()
        result = cli_runner.invoke(
            checksum.cli,
            args=[
                "test_file.txt",
                "--expected",
                "1296b08a46570840ca4fbe5d3a09d2ec35181581484a1b52b826b070d7054fd1",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "checksums match for file test_file.txt\n")

    def test_invalid_expected(self):
        cli_runner = click.testing.CliRunner()
        result = cli_runner.invoke(
            checksum.cli,
            args=[
                "test_file.txt",
                "--expected",
                "1296b08a46570840ca4fbe5d3a09d2ec35181581484a1b52b826b070d7054fd10",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(
            result.output, "checksums do not match for file test_file.txt\n"
        )


if __name__ == "__main__":
    unittest.main()
