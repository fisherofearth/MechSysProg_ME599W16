#!/usr/bin/env python


# exercise 6.8

def gcd(a, b):
    r = a % b
    #print a, b, r
    if(r == 0):
        return b
    else:
        return gcd(b, r)

if __name__ == '__main__':
    a = input('a = ')
    b = input('b = ')
    
    print 'Greatest common divisor =', gcd(a, b)
