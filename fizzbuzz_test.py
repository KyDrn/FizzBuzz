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
        actual = FizzBuzzChecker.is_fizzbuzz(6)
        self.assertEqual(actual, "Fizz")

    def test_should_return_buzz_with_multiple_of_5(self):
        actual = FizzBuzzChecker.is_fizzbuzz(10)
        self.assertEqual(actual, "Buzz")

    def test_should_return_fizzbuzz_with_multiple_of_3_and_5(self):
        actual = FizzBuzzChecker.is_fizzbuzz(15)
        self.assertEqual(actual, "FizzBuzz")

    def test_should_return_alice_number_by_default(self):
        actual = FizzBuzzChecker.is_fizzbuzz(17)
        self.assertEqual(actual, 17)

    def test_value_type(self):
        with self.assertRaises(TypeError):
            FizzBuzzChecker.is_fizzbuzz("15")
