#!/usr/bin/env python

# lab 3 - task 2
# plot 6 histograms

import matplotlib.pyplot as plt
from random import random 
import math

def summy(num):
	return sum([random() for i in xrange(10)])

if __name__ == "__main__":
	#num = input('point number =')
	time_numbers = [1e+1, 1e+2, 1e+3, 1e+4, 1e+5, 1e+6]
	plt.figure(1,figsize=(15,10))

	for t in xrange(len(time_numbers)):
		plot_num = ((len(time_numbers) /3) * 100) + 30 + 1 + t
		#print plot_num, t
		plt.subplot(plot_num)

		num = int(time_numbers[t])
		ylist = [summy(10) for i in xrange(num)]
		if len(ylist) > 50:
			bin_num = 50
		else:
			bin_num = len(ylist)

		n, bins, patches = plt.hist(ylist, bin_num, normed=True, facecolor='b', alpha=0.9)



		plt.xlabel('x')
		plt.ylabel('P(x)')
		plt.title('Hist of sum(10xrand), ' + str(int(num)) + 'times')
		plt.axis([0, 10, 0, max(n)*1.1])
		plt.grid(True)
	#print n
	#print bins


	plt.show()
