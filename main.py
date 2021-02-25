from fizzbuzz_checker import FizzBuzzChecker

def main():
    print(FizzBuzzChecker.is_fizzbuzz(6))
    print(FizzBuzzChecker.is_fizzbuzz(10))
    print(FizzBuzzChecker.is_fizzbuzz(15))
    print(FizzBuzzChecker.is_fizzbuzz(17))
    try:
        print(FizzBuzzChecker.is_fizzbuzz("15"))
    except:
        print("error not int detected")
    try:
        print(FizzBuzzChecker.is_fizzbuzz(0))
    except:
        print("error negative or zero value detected")


if __name__ == "__main__":
    main()
