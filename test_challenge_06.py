# Write a function in python that 
# takes an array of numbers and returns a
# sum of the square of all the numbers in the array.

def sum_of_squares(array_of_numbers):
    counter_sum = 0
    for number in array_of_numbers:
        square = number * number
        counter_sum = counter_sum + square
    print(counter_sum)
    return counter_sum

def test_challenge_06_happy_case(): 
     assert sum_of_squares([1,2,3,4]) == 30


def test_challenge_06_empty_array():
    assert sum_of_squares([ ]) == 0


def test_challenge_06_only_one_number_array():
    assert sum_of_squares([2,2,2,2]) == 16