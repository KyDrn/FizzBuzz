import unittest
from fizzbuzz_checker import FizzBuzzChecker

class FizzBuzzTest(unittest.TestCase):

    def test_should_raise_error_with_0(self):
        with self.assertRaises(ValueError):
            FizzBuzzChecker.is_fizzbuzz(0)
