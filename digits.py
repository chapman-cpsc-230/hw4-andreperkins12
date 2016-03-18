print """
 File: <digits.py>

Copyright (c) 2016 <Andre Perkins>

License: MIT

Machine printing the amount of numbers in the input given by the user
"""
user_input = raw_input("Enter Any Positive Integer:")
def numbers(n):
    return len(str(n))
print numbers(user_input)
