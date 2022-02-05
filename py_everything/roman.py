from typing import Dict


def convertRoman(roman: str) -> int:
    """Changes given roman numeral to the integer equivalent"""
    roman = roman.upper()  # change entered value to upper case

    rom_val: Dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    int_val: int = 0

    for i in range(len(roman)):
        if i > 0 and rom_val[roman[i]] > rom_val[roman[i - 1]]:
            int_val += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
        else:
            int_val += rom_val[roman[i]]

    return int_val
