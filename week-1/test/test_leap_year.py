import unittest
from leap_year.leap_year import is_leap_year


class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(is_leap_year(2000), True)
        self.assertEqual(is_leap_year(2016), True)
        self.assertEqual(is_leap_year(2001), False)
        self.assertEqual(is_leap_year(1900), False)
        self.assertEqual(is_leap_year(2100), False)
        self.assertEqual(is_leap_year(2400), True)
        self.assertEqual(is_leap_year(0), True)
        self.assertEqual(is_leap_year(1000), False)
