#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_char = 'I'
    roman_int = 0
    prev_roman = 0

    for roman_char in roman_string:

        current_roman = roman_dictionary.get(roman_char, 0)

        if current_roman > prev_roman:
            roman_int += current_roman - 2 * prev_roman
        else:
            roman_int += current_roman

        prev_roman = current_roman

    if not (1 <= roman_int <= 3999):
        return 0

    return roman_int
