#!/usr/bin/env python

# lab 3 - task 1
# drawing a sine curve

import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
	# user input the number of point
	num = input('point number =')

	max_x = 4. * math.pi

	xlist = [(max_x * i) / num for i in xrange(num)]
	ylist = [math.sin(x) for x in xlist]

	plt.plot(xlist, ylist)
	plt.xlabel('x')
	plt.ylabel('sin(x)')
	plt.title('A sine curve')
	plt.show()