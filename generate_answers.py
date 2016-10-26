#! usr/bin/python3

import re
import read_file
import understand_numerals_earth
import understand_numerals_roman
import calulate_merchants_units

def get_answers (info, currency, price):
    # LOOP through Dictionary returned from read_file.py
    for key, value in info.items():
        # Find Questions Key
        if (key == 'Questions'):
            for question in value:
                # Varibales to store later ascertained info from Questions
                roman_sum = ''
                words_total = ''
                material = ''
                
                # Search through Questions to eliminate irrelevent Questions
                # From the start of the line
                # And finds the first question that doesn't deal with
                # 'Minerals / non-defined' values
                if (re.search(r'^how much is', question)) != None:
                    # split Question strings into Array then Loop
                    for words in question.split(' '):
                        if (words in currency):
                            # If word exists when lookuped in the curreny
                            # Dictionary returned from understand_numerals_roman.py
                            # assign value to valuerance variable
                            valuerance = currency[words]
                            # To structure the response string with the words we 
                            # found in Questions
                            words_total = words_total.join(['' ,words]) + ' '
                            # We join up all the values for the merchants
                            # currency in roman numerals
                            roman_sum = roman_sum.join(['', valuerance])
                    # We interprut roman_sum with understand_numerals_earth.py
                    # and return a earth readable value
                    earth_sum = understand_numerals_earth.understand_numerals_earth(roman_sum)
                    # Structure sentence and print out to terminal
                    print (words_total, 'is', earth_sum)
                
                # Looks at the remainder of the questions
                elif (re.search(r'^how many Credits is', question)) != None:
                    for words in question.split(' '):
                        # Same explinination as above but with a second step
                        # detailed in the second if block of code
                        if (words in currency):
                            valuerance = currency[words]
                            words_total = words_total.join(['', words]) + ' '
                            roman_sum = roman_sum.join(['', valuerance])
                            
                        earth_sum = understand_numerals_earth.understand_numerals_earth(roman_sum)
                        
                        # From calulate_merchants_units.py we have a price Dictionary
                        # which holds the values for 'Minerals / non-defined' values
                        # We lookup a word in this Dictionary and retrieve the
                        # respected values
                        if (words in price):
                            material_price = price[words]
                            material = words
                            total_price = earth_sum * material_price

                    # We use int() func from Python to change the decimal value
                    # to an integer for the respose
                    print (words_total, material, 'is', int(total_price), 'Credits')
                        
                else:
                    # Slight error handling for the random questions asked
                    print ('I have no idea what you are talking about')

if (__name__ == "__main__"):
    info = read_file.read_file('ThoughtWorks.txt')
    currency = understand_numerals_roman.understand_numerals_roman(info)
    get_price = calulate_merchants_units.calulate_merchants_units(info, currency)
    get_answers(info, currency, get_price)