# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    vowels = ("a", "e", "i", "o", "u","A","E", "I","O","U")
    number_of_vowels = 0
    for letter in word:
        if letter in vowels:
          number_of_vowels = number_of_vowels +1
    return number_of_vowels
    print(number_of_vowels)


def test_challenge_01_happy_case():
     assert count_vowels('Kaleidoscope') == 6


def test_challenge_01_empty_string():
    assert count_vowels(' ') == 0


def test_challenge_01_without_vowel():
    assert count_vowels('bcdfg') == 0


def test_challenge_01_with_only_vowels():
    assert count_vowels('AaEeiEoOuU') == 10

def test_challenge_01_spaces_between():
    assert count_vowels('Aa Ee iEo O uU') == 9
