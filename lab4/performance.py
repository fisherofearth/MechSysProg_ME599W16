#!/usr/bin/env python

from bubblesort import *
from insertionsort import *
from quicksort import quicksort
import matplotlib.pyplot as plt
from lib_lab4 import *


if __name__ == '__main__':
	test_times = 1
	# [100, 200, ... 2000]
	length_list = [(l+1)*100 for l in xrange(20)]

	timer_buildin =[]
	timer_bubble = []
	timer_quicksort=[]
	timer_insertion = []

	for length in length_list:
		#generate a list
		unsorted_list = generateRandomNum(length)
		timer_buildin.append(average_timer(sorted,unsorted_list,test_times))
		timer_bubble.append(average_timer(bubbltsort,unsorted_list,test_times))
		timer_quicksort.append(average_timer(quicksort,unsorted_list,1))
		timer_insertion.append(average_timer(insertionsort,unsorted_list,test_times))
	#plot
	plt.figure(1)

	plt.plot(length_list, timer_buildin, label = 'build-in sorted')
	plt.plot(length_list, timer_bubble, label = 'bubblesort')
	plt.plot(length_list, timer_quicksort, label = 'quicksort')
	plt.plot(length_list, timer_insertion, label = 'insertionsort')
	plt.title('build-in sorted, bubble sort, insertion sort')
	plt.xlabel('length of list')
	plt.ylabel('time(sec)')
	plt.axis([ min(length_list), max(length_list), 0 , max(timer_buildin + timer_bubble + timer_insertion)])
	plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)

	plt.show()

