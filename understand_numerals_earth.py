#! usr/bin/python3

import re

def understand_numerals_earth (RomanStr):
	# Basics of the Roman Numeral Algorithm
	# "C" can be subtracted from "D" and "M" only, etc. (view README.md)
	# Regex to search the entire string
	# http://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
	if (re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', RomanStr)) != None:
		# Dictionary to track pattern
		pattern_track = { 
    		"pattern": "", 
    		"num_count": 0 
    	}
		
		# The Numerals that can be repeated or subtracted from
		# So that certain values can't not be strung together
		# To assess a valid Roman Numeral
		roman_pattern = { 
			"0": ('','','','M'), 
			"1": ('CM','CD','D','C',100), 
			"2": ('XC','XL','L','X',10), 
			"3": ('IX','IV','V','I',1) 
		}
		
		# Roman Numeral can't be larger than 4 digits
		i = 3
		# To keep the Directory in logical order when looping over
		sorted_roman_num = sorted(roman_pattern.items())

		# Loop through roman_pattern keys
		for roman_items in sorted_roman_num:
			# Map out the pattern and track count of values
			if (roman_items[0] != '0'):
				pattern_str = pattern_track["pattern"].join(['',roman_items[1][0]])
				if (re.search(pattern_str, RomanStr)) != None:
					# CM would equal 900 (M - C) = (1000 - 100)
					pattern_track["num_count"] += 9*roman_items[1][4]
					pattern_track["pattern"] = pattern_str
				else:
					# Add to pattern string
					pattern_str = pattern_track["pattern"].join(['',roman_items[1][1]])
					if (re.search(pattern_str, RomanStr)) != None:
						# CD would equal 400 (D - C) = (500 - 100)
						pattern_track["num_count"] += 4*roman_items[1][4]
						pattern_track["pattern"] = pattern_str
					else:
						# Add to pattern string
						pattern_str = pattern_track["pattern"].join(['',roman_items[1][2]])
						if (re.search(pattern_str, RomanStr)) != None:
							# D equal 500
							pattern_track["num_count"] += 5*roman_items[1][4]
							pattern_track["pattern"] = pattern_str
							
			if (pattern_track["pattern"] == ''):
				pattern_track["pattern"] = '^'
			tempstr = ''
			
			# Roman Numeral can't be larger than 4999
			sum = 0
			# System of elimination
			for k in range(0,4):
				pstr = roman_items[1][3] + '{' + str(k) + '}'
				#pstr = roman_items[1][3].join(['','{']).join(['',str(k)]).join(['','}'])
				pattern_str = pattern_track["pattern"].join(['',pstr])
				# find input values within patterns and eliminate what is not
				if (re.search(pattern_str, RomanStr)) != None:
					sum = k*(10**i)
					tempstr = pattern_str
			if (tempstr != ''):
				pattern_track["pattern"] = tempstr
			else:
				pattern_track["pattern"] = pattern_str

			# Total value
			pattern_track['num_count'] += sum
			i -= 1
		return pattern_track['num_count']
	else:
		print ('String is not a valid Roman numerals')

# Used to run the script in isolation for testing
# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if (__name__ == "__main__"):
    understand_numerals_earth('CMVI')