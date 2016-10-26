#! /usr/bin/python3

# This file is not operational
# TO-DO update my merchants Dictionary with each merchant I meet

import read_file

def add_new_trade_info (visited_merchants):
    for planet, currency in visited_merchants.items():
        if (visited_merchants):
            currencies.update({planet: currency})
    return currencies
    
if (__name__ == "__main__"):
    info = read_file.read_file()
    add_new_trade_info(info)