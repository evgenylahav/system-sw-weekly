"""
unit test for password generator module
"""
import unittest
from unittest.mock import patch
from password_generator.generate_password import password_generator
from tests import mock_counter


class TestGeneratePassword(unittest.TestCase):
    """
    Test class
    """
    def test_password_length(self):
        """ Testing password length """
        password = password_generator(16)
        self.assertEqual(len(password), 16)
        password = password_generator(30)
        self.assertEqual(len(password), 30)
        password = password_generator(1)
        self.assertEqual(len(password), 1)

        self.assertRaises(Exception, password_generator, 0)

    @patch('random.randint', mock_counter.Random(33))
    def test_password_generator1(self):
        """ Testing password generator with mock """
        password = password_generator(32)
        self.assertEqual(password, '"#$%&\'()*+,-./0123456789:;<=>?@A')

    @patch('random.randint', mock_counter.Random(55))
    def test_password_generator2(self):
        """ Testing password generator with mock """
        password = password_generator(32)
        self.assertEqual(password, '89:;<=>?@ABCDEFGHIJKLMNOPQRSTUVW')


if __name__ == '__main__':
    unittest.main()
