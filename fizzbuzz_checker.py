class FizzBuzzChecker:
    
    @staticmethod
    def is_fizzbuzz(number):
        if type(number) is not int:
            raise TypeError
        if number <= 0:
            raise ValueError
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        else:
            return number
            
