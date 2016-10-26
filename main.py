#! usr/bin/python3

import os
import read_file, understand_numerals_roman, understand_numerals_earth, calulate_merchants_units, generate_answers

def main():
    info = read_file.read_file("ThoughtWorks.txt")
    currency = understand_numerals_roman.understand_numerals_roman(info)
    get_price = calulate_merchants_units.calulate_merchants_units(info, currency)
    generate_answers.get_answers(info ,currency, get_price)
    
if (__name__ == "__main__"):
    main()