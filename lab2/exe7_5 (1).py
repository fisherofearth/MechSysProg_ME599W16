#!/usr/bin/env python

# exercise 7.5

import math
from math import factorial


def estimate_pi():
    S = 0.
    c = (2. * math.sqrt(2.)) / 9801.
    k = 0.
    last_term = 1.
    while(last_term > (1e-15)):
        M = factorial(4. * k) * (1103. + (26390. * k))
        N = (factorial(k) ** 4.) * (396. ** (4. * k))
        last_term = c * (M/N)
        S = S + last_term
        k = k + 1.
        #print k, last_term
    return (1./(S))

if __name__ == '__main__':
    print 'math.pi      =', math.pi
    print 'estimated pi =', estimate_pi()
