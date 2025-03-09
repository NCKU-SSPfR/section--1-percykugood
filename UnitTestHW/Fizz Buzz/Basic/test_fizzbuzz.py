from horrible_fizzbuzz import fizzBuzz

def test_3():
    assert fizzBuzz(3) == "Fizz"

def test_5():
    assert fizzBuzz.singleFizzBuzz(5) == "Buzz"

def test_15():
    assert fizzBuzz.singleFizzBuzz(15) == "FizzBuzz"

def test_2():
    assert fizzBuzz.singleFizzBuzz(2) == "2"
