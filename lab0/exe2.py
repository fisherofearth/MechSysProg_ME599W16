#!/usr/bin/python

num = (float)(input('Quantity = '))

shipCost = 3 + ((num - 1) * 0.75)
wholesaleCost = shipCost + (num * (24.95 * 0.6))

print 'Wholesale cost = '  + str(wholesaleCost)
