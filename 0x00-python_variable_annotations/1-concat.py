#!/usr/bin/env python3
"""Write a type-annotated function concat that takes a string str1 and a
string str2 as arguments and returns a concatenated string
"""

def concat(str1: str, str2: str) -> str:
    """Concatenate two strings"""
    return str1 + str2

if __name__ == '__main__':
    
    str1 = 'Smart'
    str2 = 'Empire'

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)