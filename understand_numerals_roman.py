#! usr/bin/python3

import read_file

def understand_numerals_roman (info):
    # Can increase in more Questions / Info entered
    # TO-DO Makes Dynamic
    translate_to_roman = [[],[],[],[],[],[],[]]
    currency = {}

    # LOOP through Dictionary returned in read_file.py
    for key, value in info.items():
        # Find key which holds the Conditions in the inputted text file
        if (key == 'Currency'):
            # enumerate used to better understand values for iteration
            # and creates a Dictionary with index 0 and increments
            for index, number in enumerate(value):
                # used index to Conditions and split for better manipulation
                # of merchants currencies to roman numerals
                translate_to_roman[index] = number.split()

    for i in translate_to_roman:
        # If there is a value in translate_to_roman add to
        # currency Dictionary
        if (i):
            currency[i[0]] = i[2]
    return currency
	
if (__name__ == "__main__"):
    info = read_file.read_file('ThoughtWorks.txt')
    understand_numerals_roman(info)