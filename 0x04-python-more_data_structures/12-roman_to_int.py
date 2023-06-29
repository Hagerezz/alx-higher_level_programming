#!/usr/bin/python3
def get_subtraction_value(numbers_list):
    subtraction_value = 0
    max_number = max(numbers_list)
    for number in numbers_list:
        if max_number > number:
            subtraction_value += number
    return max_number - subtraction_value


def roman_to_integer(roman_numeral_string):
    if not roman_numeral_string:
        return 0
    if not isinstance(roman_numeral_string, str):
        return 0
    roman_numeral_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_numeral_keys = list(roman_numeral_dict.keys())
    integer_value = 0
    last_roman_numeral = 0
    numbers_list = [0]
    for numeral in roman_numeral_string:
        for numeral_key in roman_numeral_keys:
            if numeral_key == numeral:
                if roman_numeral_dict.get(numeral) <= last_roman_numeral:
                    integer_value += get_subtraction_value(numbers_list)
                    numbers_list = [roman_numeral_dict.get(numeral)]
                else:
                    numbers_list.append(roman_numeral_dict.get(numeral))
                last_roman_numeral = roman_numeral_dict.get(numeral)
    integer_value += get_subtraction_value(numbers_list)
    return integer_value
