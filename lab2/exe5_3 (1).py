#!/usr/bin/env python


#exercise 5.3

def check_fermat(a, b, c, n):
    if(n<=2):
        print 'Error! n must be greater than 2.'
        return 'error'
    if(a<=0 or b<=0 or c<=0):
        print 'Error! a, b and c must be positive.'
        return 'error'
    left = (a ** n) + (b ** n)
    right = c ** n
    if left == right:
        return True
    else:
        return False

if __name__ == '__main__':
    a = input('a = ')
    b = input('b = ')
    c = input('c = ')
    n = input('n = ')
    
    result = check_fermat(a, b, c, n) 
    if( result == True):
        print "Holy smokes, Fermat was wrong!"
    elif(result == False):
        print "No, that doesn't work"
    

    
