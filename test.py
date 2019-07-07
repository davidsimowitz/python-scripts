"""Unit tests"""


import checksum
import unittest


class TestChecksum(unittest.TestCase):

    def test_valid_checksum(self):
        self.assertTrue(checksum.checksum(
          filename='test_file.txt',
          expected='b93c5dc9875af15ffe00f5004bd2c13927a522116c40e9a9ed74c127a0df1660'
          )
        )

    def test_invalid_checksum(self):
        self.assertFalse(checksum.checksum(
          filename='test_file.txt',
          expected='6a59087a7a99e8670920f2ecdd464e31c4f01cf3d38e8338e5b6c21069cca323'
          )
        )


if __name__ == "__main__":
    unittest.main()
