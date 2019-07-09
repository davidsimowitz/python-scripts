"""Unit tests"""


import checksum
import unittest


class TestChecksum(unittest.TestCase):

    def test_valid_checksum(self):
        self.assertTrue(
          checksum.checksum(
            filename='test_file.txt',
            expected=checksum.calc_checksum('test_file.txt')
          )
        )

    def test_invalid_checksum(self):
        self.assertFalse(
          checksum.checksum(
            filename='test_file.txt',
            expected=checksum.calc_checksum('test_file.txt') + '0'
          )
        )


class TestChecksumCli(unittest.TestCase):

    def test_valid_checksum(self):
        self.assertEqual(
          checksum.cli(
            filename='test_file.txt',
            expected_checksum=checksum.calc_checksum('test_file.txt')
          ),
          'checksums match for file test_file.txt'
        )

    def test_invalid_checksum(self):
        self.assertEqual(
          checksum.cli(
            filename='test_file.txt',
            expected_checksum=checksum.calc_checksum('test_file.txt') + '0'
          ),
          'checksums do not match for file test_file.txt'
        )


if __name__ == "__main__":
    unittest.main()
