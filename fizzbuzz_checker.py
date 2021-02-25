class FizzBuzzChecker:
    
    @staticmethod
    def is_fizzbuzz(number):
        if number <= 0:
            raise ValueError
        if number == 6:
            return "Fizz"
        else:
            return "Buzz"
            
