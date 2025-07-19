#!/bin/python3

import re

# Complete the solve function below.
def solve(s: str) -> str:
    result = ''
    previous_char = ' '
    if not s:
        return ''
    for letter in s:
        if previous_char == ' ' and letter.isalpha():
            result += letter.upper()
        else:
            result += letter.lower()
        previous_char = letter
    return result

def solve2(s: str) -> str:
    
    return re.sub(r'\b([a-z])', lambda m: m.group(1).upper(), s.lower())

def solve3(s: str) -> str:
    return ''.join(
        char.upper() if (i == 0 or s[i-1] == ' ') and char.isalpha() 
        else char.lower() if char.isalpha() 
        else char
        for i, char in enumerate(s)
    )

def solve4(s: str) -> str:
    return ''.join(c.upper() if i == 0 or s[i-1] == ' ' and c.isalpha() else c.lower() for i, c in enumerate(s))

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
