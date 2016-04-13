#!/usr/bin/env python

# lab 3 - task 4

import time
from random import random
import matplotlib.pyplot as plt

def generate_a_list(list_length):
	return [random() for i in xrange(list_length)]


def timer(fun, listName):
	start = time.clock()
	fun(listName)
	end = time. clock()

	return (end - start)


if __name__ == "__main__":
	lengths = [10**x for x in xrange(7)]
	time_sum = []
	time_sort = []

	print '======================================='
	print 'length |  sort time | sum time'
	print '---------------------------------------'
	for length in lengths:
		time_sort.append(timer(sorted, generate_a_list(length)))
		time_sum.append(timer(sum, generate_a_list(length)))

	for i in xrange(len(lengths)):
		print ('1e+' + str(i)) , '  | ', float(time_sort[i]), ' | ', float(time_sum[i])
	print '======================================='

	# plot
	plt.figure(1)
	plt.plot(range(len(lengths)), time_sort, 'ro-', label = 'sort time')
	plt.plot(range(len(lengths)), time_sum, 'bo-', label = 'sum time')
	plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=1.)
	#plt.plot(t, state)
	plt.title('build-in function timer test')
	plt.xlabel('test number')
	plt.ylabel('time(second)')
	plt.show()