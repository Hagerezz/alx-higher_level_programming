#!/usr/bin/python3
def tosub(list_n):
    to_su = 0
    max_l = max(list_n)
    for i in list_n:
        if max_l > i:
            to_su += i
    return (max_l - to_su)

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_key = list(rom_n.key())
    nu = 0
    last_ro = 0
    list_nu = [0]
    for c in roman_string:
        for r in list_key:
            if r == c:
                if rom_n.get(c) <= last_ro:
                    nu += to_subtract(list_nu)
                    list_nu = [rom_n.get(c)]
                else:
                    list_nu.append(rom_n.get(c))
                last_ro = rom_n.get(c)
    nu += to_subtract(list_nu)
    return (nu)
