import unittest
from hypothesis import given, example, assume
from hypothesis.strategies import integers
from leap_year import is_leap_year
import calendar


class TestLeapYear(unittest.TestCase):
    @example(year=2000)
    @example(year=2016)
    @example(year=1900)
    @example(year=0)
    @given(integers())
    def test_is_leap_year(self, year):
        assume(year >= 0)
        print('Testing year = {}'.format(str(year)))
        self.assertEqual(is_leap_year(year), calendar.isleap(year))

    # def test_leap_year(self):
    #     self.assertEqual(is_leap_year(2000), True)
    #     self.assertEqual(is_leap_year(2016), True)
    #     self.assertEqual(is_leap_year(2001), False)
    #     self.assertEqual(is_leap_year(1900), False)
    #     self.assertEqual(is_leap_year(2100), False)
    #     self.assertEqual(is_leap_year(2400), True)
    #     self.assertEqual(is_leap_year(0), True)
    #     self.assertEqual(is_leap_year(1000), False)


"""
Testing year = 2000
Testing year = 2016
Testing year = 1900
Testing year = 0
Testing year = 0
Testing year = 647724030
Testing year = 12495
Testing year = -5618
Testing year = -178802352
Testing year = 4106369718108303117
Testing year = -1032
Testing year = 5
Testing year = 12563
Testing year = 7
Testing year = 29929
Testing year = 0
Testing year = 0
Testing year = 0
Testing year = 0
Testing year = -127
Testing year = -22287
Testing year = -127
Testing year = 106
Testing year = -827093753
Testing year = 55
Testing year = 0
Testing year = 14960
Testing year = -7661
Testing year = 20926
Testing year = 6863
Testing year = -25232
Testing year = 77
Testing year = 1920
Testing year = 21086
Testing year = 4036
Testing year = 0
Testing year = 1730468002
Testing year = 0
Testing year = 19050
Testing year = 768
Testing year = -52006768333802999115455144216290549806
Testing year = 27834
Testing year = 0
Testing year = -362124693
Testing year = 13848
Testing year = 0
Testing year = -48
Testing year = 2112750869
Testing year = -373226590472022297
Testing year = -5428
Testing year = -19660
Testing year = 58
Testing year = -15
Testing year = 32078
Testing year = 21778
Testing year = 453
Testing year = 74
Testing year = 11978
Testing year = -18347
Testing year = 7924
Testing year = -60
Testing year = -52
Testing year = 0
Testing year = 21504
Testing year = 4381
Testing year = 0
Testing year = -2
Testing year = 2052643708
Testing year = -93
Testing year = -8461
Testing year = -41
Testing year = 20
Testing year = 231373164
Testing year = 20736
Testing year = 6213
Testing year = -1936
Testing year = 0
Testing year = -95
Testing year = 1870544493
Testing year = -8773685071875660449
Testing year = -18293
Testing year = 28291
Testing year = -29
Testing year = 6
Testing year = -15965
Testing year = 2122853962
Testing year = -15805
Testing year = 94
Testing year = 8131
Testing year = 0
Testing year = 0
Testing year = -24292
Testing year = 2
Testing year = 0
Testing year = 0
Testing year = -24847
Testing year = -29835
Testing year = -922162224
Testing year = 1875172643
Testing year = -19923
Testing year = 29549
Testing year = 0
Testing year = -28620
Testing year = -5068
"""

if __name__ == '__main__':
    unittest.main()
