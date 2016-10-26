#! /usr/bin/python3

import re
import currency

def read_file (info):
    # TO-DO
    # Add Planet Names based on the text file supplied
    # planet_name = trade_info.split('.')
    
    # Keep track of the content from the files
    # TO-BE converted to dictionary with Planet Name as key
    # TO-DO move to a DB like Mongo or Orient
    visited_merchants = {
                            'Currency': [],
                            'Conditions': [],
                            'Questions': []
                        }
    
    # OPEN file
    with open(info, 'r') as f:
            # Break file into lines
            for line in f:
                # Convert line to Array for easier manipulation
                lines = line.split(' ')
                # A variable to change Array to Strings when needed
                content = ''
                # Find all lines which are questions
                if ( lines[-1].rstrip() == '?' ):
                    visited_merchants['Questions'].append(str.join(' ', lines))
                # Everyhting else is dumoped into conditions for now
                else:
                    visited_merchants['Conditions'].append(str.join(' ', lines))
                
                # Loop through each line in Conditions to remove or add
                # values to respectful keys
                for condition in visited_merchants['Conditions']:
                    for numeral in currency.currenices['Roman'].keys():
                        # If Roman Numeral exists then remove line from
                        # Conditions and add to Currency
                        if ( lines[2].rstrip() == numeral ):
                            visited_merchants['Conditions'].remove(condition)
                            visited_merchants['Currency'].append(condition)
    
    return visited_merchants

if (__name__ == "__main__"):
    read_file("ThoughtWorks.txt")