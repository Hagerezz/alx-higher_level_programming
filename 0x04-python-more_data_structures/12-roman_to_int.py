#!/usr/bin/python3
def get_subtraction_value(numbers):
    subtract_total = 0
    max_num = max(numbers)

    subtract_total = sum(filter(lambda n: max_num > n, numbers))

    return (max_num - subtract_total)


def roman_to_int(roman_numeral):
    if not isinstance(roman_numeral, str):
        return 0
    roman_numerals_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_numeral = 0
    numerals = [0]
    for numeral in roman_numeral:
        if numeral not in roman_numerals_dict:
            return 0
        if roman_numerals_dict[numeral] > last_numeral:
            num += get_subtraction_value(numerals)
            numerals = [roman_numerals_dict[numeral]]
        else:
            numerals.append(roman_numerals_dict[numeral])

        last_numeral = roman_numerals_dict[numeral]
    num += get_subtraction_value(numerals)
    return num
