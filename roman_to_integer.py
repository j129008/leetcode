roman_one_char = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_two_char = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}


def romanToInt(s):
    roman_int = 0
    while s != '':
        if s[:2] in roman_two_char:
            roman_int += roman_two_char[s[:2]]
            s = s[2:]
        else:
            roman_int += roman_one_char[s[0]]
            s = s[1:]
    return roman_int

print(romanToInt('IVVVV'))

