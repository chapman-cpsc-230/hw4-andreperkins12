print """
 File: <smoothheaviside.py>

Copyright (c) 2016 <Andre Perkins>

License: MIT

Testing H_eps
"""

import math
def H_eps(x, eps = 0.01):
    result = 0
    if x < -eps:
        result = 0
    elif x <= eps:
        result = 0.5 + (x/(2 * eps)) + ((1/2 * math.pi) * math.sin(math.pi * x )/ eps)
    else:
        result = 1
    return result

def test_H_eps():
    print "-1", H_eps(-1)
    print "-0.01", H_eps(-0.01)
    print "0", H_eps(0)
    print "0.01", H_eps(0.01)
    print "1", H_eps(1)

test_H_eps()
