#! usr/bin/python3

# This file is not operational currently
# TO-DO more dynamic approach to the Roman Algorithm

import re
import currency

def roman_algorithm(RomanStr):
    cant_be_opertor = ('V', 'L', 'D')
    subtract_rules = { 'C': ['D', 'M'], 'I': ['V', 'X'], 'X': ['L', 'C'] }
    can_be_repeated = ('I', 'X', 'C', 'M')
    
    roman_numerals = currency.currenices['Roman']
    roman_str = list(RomanStr)
    
    for num, val in roman_numerals.items():
        for numeral in roman_str:
            if ( numeral == num ):
                if ( numeral in cant_be_opertor ):
                    print (numeral)

if __name__ == "__main__":
    roman_algorithm('MCMXLIV')