class FizzBuzzChecker:
    
    @staticmethod
    def is_fizzbuzz(number):
        if number <= 0:
            raise ValueError
        else:
            return "Fizz"
