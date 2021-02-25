import unittest
from fizzbuzz_checker import FizzBuzzChecker

class FizzBuzzTest(unittest.TestCase):

    def test_should_raise_error_with_0(self):
        with self.assertRaises(ValueError):
            FizzBuzzChecker.is_fizzbuzz(0)

    def test_should_raise_error_with_negative_value(self):
        with self.assertRaises(ValueError):
            FizzBuzzChecker.is_fizzbuzz(-1)
    
    def test_should_return_fizz_with_multiple_of_3(self):
        with self.assertEqual("Fizz"):
            FizzBuzzChecker.is_fizzbuzz(6)
