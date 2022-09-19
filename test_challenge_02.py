# Create a Python function that accepts a string. 
# The function should return a string, with each 
# character in the original string doubled. 
# If you send the function "now" as a parameter, 
# it should return "nnooww," and if you send "123a!", 
# it should return "112233aa!!".

def duplicate_characters(string):
    duplicated_string = ""
    for letter in string:
        duplicated_string = duplicated_string + letter * 2
    return duplicated_string


duplicate_characters("maria")


def test_challenge_02_case_1(): 
     assert duplicate_characters('now') == 'nnooww'

def test_challenge_02_case_2(): 
     assert duplicate_characters('123a!') == '112233aa!!'


def test_challenge_02_numbers():
    assert duplicate_characters('487') == '448877'


def test_challenge_02_empty():
    assert duplicate_characters('') == ''