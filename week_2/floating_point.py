import re

def is_valid_float(s):
    pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*)$'
    return bool(re.match(pattern, s))

# Input number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Input string
    s = input()
    # Check if the string is a valid floating point number and print the result
    print(is_valid_float(s))
