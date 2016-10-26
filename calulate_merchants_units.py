#! usr/bin/python3

import re
import read_file
import understand_numerals_roman
import understand_numerals_earth

def calulate_merchants_units (info, currency):
    price = {}
    
    for key, value in info.items():
        # Find Conditions key in Dictionary generated from read_file.py
        if (key == 'Conditions'):
            # Loop over each value of Conditions
            for condition in value:
                # Declared varibales for later assignment
                roman_sum = ''
                earth_sum = ''
                value_number = 0
                
                # Find the 'Minerals' / 'non-defined values' in Conditions
                for temp in ['Silver','Gold','Iron']:
                    if (re.search(temp, condition)) != None:
                        # string to Array for better manipulation by splitting
                        # on 'Minerals' / 'non-defined values'
                        sentense = condition.split(temp)
                        
                        # First values in sentenses after 'split of temp'
                        for i in sentense[0].split(' '):
                            if (i):
                                # If value exists we lookup in the curreny
                                # Dictionary returned from understand_numerals_roman.py
                                # assign to roman variable
                                roman = currency[i]
                                # Sum the found / translated roman numerals
                                roman_sum = roman_sum.join(['',roman])
                                # Translate roman numerals to earth values
                                earth_sum = understand_numerals_earth.understand_numerals_earth(roman_sum)

                        # Second values in sentenses after 'split of temp'
                        for i in sentense[1].split(' '):
                            # Find digit rather than using regex
                            if (i.isdigit()):
                                # Convert digit to decimal value for later manipulation
                                value_number = float(i)
                        
                        # temp value = 'Minerals' / 'non-defined values'
                        # assign an key in price with condition value calculated
                        price[temp] = value_number / earth_sum
    return price

if (__name__ == "__main__"):
    info = read_file.read_file('ThoughtWorks.txt')
    currency = understand_numerals_roman.understand_numerals_roman(info)
    calulate_merchants_units(info, currency)