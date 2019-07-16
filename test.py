"""Unit tests"""


import checksum
import click.testing
import unittest


class TestChecksum(unittest.TestCase):
    def test_valid_checksum(self):
        self.assertTrue(
            checksum.checksum(
                filename="test_file.txt",
                expected_checksum=checksum.calc_checksum(filename="test_file.txt"),
            )
        )

    def test_invalid_checksum(self):
        self.assertFalse(
            checksum.checksum(
                filename="test_file.txt",
                expected_checksum=checksum.calc_checksum(filename="test_file.txt")
                + "0",
            )
        )


class TestChecksumCli(unittest.TestCase):
    def test_valid_checksum(self):
        cli_runner = click.testing.CliRunner()
        result = cli_runner.invoke(
            checksum.cli,
            args=["test_file.txt", checksum.calc_checksum(filename="test_file.txt")],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "checksums match for file test_file.txt\n")

    def test_invalid_checksum(self):
        cli_runner = click.testing.CliRunner()
        result = cli_runner.invoke(
            checksum.cli,
            args=[
                "test_file.txt",
                checksum.calc_checksum(filename="test_file.txt") + "0",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(
            result.output, "checksums do not match for file test_file.txt\n"
        )


if __name__ == "__main__":
    unittest.main()
