"""
examples to using hypothesis
https://hypothesis.readthedocs.io/en/latest/quickstart.html
"""
import unittest
from hypothesis import given, example
from hypothesis.strategies import text
from rosetta import encode, decode


class TestRosetta(unittest.TestCase):
    @example(s='')
    @example(s='00/')
    @given(text())
    def test_decode_inverts_encode(self, s):
        self.assertEqual(decode(encode(s)), s)


if __name__ == '__main__':
    unittest.main()
