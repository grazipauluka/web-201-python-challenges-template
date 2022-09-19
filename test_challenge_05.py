# Write a function in Python that accepts a list of 
# any length that contains a mix of non-negative 
# integers and strings. The function should return 
# a list with only the integers in the original 
# list in the same order.

def extract_integers(mixed_list):
    list_integers = []
    for item in mixed_list:
        try:
            int_value = int(item)
        except ValueError:
            pass
        else:
            list_integers.append(int_value)
    print(list_integers)
    return list_integers



extract_integers([1, 'apple', 2, 'banana',3, 4])
def test_challenge_05_happy_case(): 
     assert extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]


def test_challenge_05_only_strings():
    assert extract_integers(['apple', 'banana']) == [ ]


def test_challenge_05_only_numbers():
    assert extract_integers([1, 2, 3, 4]) == [1, 2, 3, 4]