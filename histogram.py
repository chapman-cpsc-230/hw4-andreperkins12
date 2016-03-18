print """
 File: <histogram.py>

Copyright (c) 2016 <Andre Perkins>

License: MIT

Ls to represent a list. We define bar to attach a string to star so that
 for the values inside the list will be represented by stars
"""

ls = [4, 9, 13, 5]

def bar(n):
    st = ''
    for i in range(n):
        st += '*'
    return st

for i in range(len(ls)):
    print bar(ls[i])
print ls
