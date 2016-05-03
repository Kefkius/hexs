import unittest

from hexs import is_hex, format_hex, hexs

class IsHexTest(unittest.TestCase):
    def test_is_hex(self):
        self.assertTrue(is_hex('2'))
        self.assertTrue(is_hex('0xf'))

    def test_is_not_hex(self):
        self.assertFalse(is_hex('0xg'))
        self.assertFalse(is_hex(5))

class FormatHexTest(unittest.TestCase):
    def test_format_hex(self):
        self.assertEqual('07', format_hex('0x7'))
        self.assertEqual('01ff', format_hex('1ff'))
        self.assertEqual('0528', format_hex('0528'))

class HexsTest(unittest.TestCase):
    def test_hexs(self):
        self.assertEqual('07', hexs(7))
        self.assertEqual('0100', hexs(256))
