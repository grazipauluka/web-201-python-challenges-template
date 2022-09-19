from math import floor

# It takes 21 seconds to wash your hands
# and help prevent the spread of COVID-19.
#
# Create a function that takes the number of times 
# a person washes their hands per day (n) 
# and the number of months (m) they follow this routine, 
# and calculates the duration in minutes and seconds 
# that person spends washing their hands.
#
# Examples:
# wash_hands(8, 7) ➞ "588 minutes and 0 seconds"
# wash_hands(0, 0) ➞ "0 minutes and 0 seconds"
# wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
# 
# Notes: Consider a month has 30 days.

def wash_hands(n, m):
    seconds_to_wash = 21
    secondes_in_one_minute = 60
    time_per_day = n * seconds_to_wash
    days_whasing = 30 * m
    time_washing_seconds = (time_per_day * days_whasing) % secondes_in_one_minute
    time_washing_minutes = (time_per_day * days_whasing) / secondes_in_one_minute
    time_washing_minutes = floor(time_washing_minutes)
    print(f'{time_washing_minutes} minutes and {time_washing_seconds} seconds')
    return (f'{time_washing_minutes} minutes and {time_washing_seconds} seconds')





def test_challenge_03_case_1():
    assert wash_hands(8, 7) == '588 minutes and 0 seconds'


def test_challenge_03_case_0():
    assert wash_hands(0, 0) == '0 minutes and 0 seconds'


def test_challenge_03_case_3():
    assert wash_hands(7, 9) == '661 minutes and 30 seconds'

wash_hands(8,7)
wash_hands(0,0)
wash_hands(1,1)