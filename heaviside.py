
"""
File: <heavyside.py>
Copyright (c) 2016 <Andre Perkins>
License: MIT
<program to test the value >
"""

import math
def H_eps(x, eps = 0.01):
    if x < -eps:
        result = 0
    elif x <= eps:
        result = 0.5 *(1 + x/eps + 1.0/pi * sin(pi*(x/eps)))
    else:
        result = 1
    return result

def H(x):
    if x < 0:
        value = 0
    if x >= 0:
        value = 1
    return value


def test_H():
    if H(10)!= 1:
        print "error"
    if H(-10**-15) != 0:
        print "error"
    if H(-10) != 0:
        print 'error'
    if H(10**15) != 1:
        print 'error'
    else:
        print "correct"
test_H()
