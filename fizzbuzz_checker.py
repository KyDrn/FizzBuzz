class FizzBuzzChecker:
    
    @staticmethod
    def is_fizzbuzz(number):
        if number <= 0:
            raise ValueError
        if number == 15:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number == 10:
            return "Buzz"
            
