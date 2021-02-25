class FizzBuzzChecker:
    
    @staticmethod
    def is_fizzbuzz(number):
        if number <= 0:
            raise ValueError
        if number % 3 == 0:
            return "Fizz"
        else:
            return "Buzz"
            
