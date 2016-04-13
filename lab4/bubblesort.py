#!/usr/bin/env python


# bubblesort and timing
from lib_lab4 import *

def bubbltsort(unsorted_list):
	sortedL=list(unsorted_list)
	for i in xrange(len(unsorted_list)-1):
		for j in xrange(len(unsorted_list) -i-1):
			if (sortedL[j+1]< sortedL[j]):
				(sortedL[j+1], sortedL[j]) = (sortedL[j], sortedL[j+1])
	return sortedL


if __name__ == '__main__':

	len_list = input('length of list = ')

	#generate a list
	unsorted_list = generateRandomNum(len_list)
	

	
	sorted_list = bubbltsort(unsorted_list)

	#print unsorted_list
	#print sorted_list

	print average_timer(bubbltsort,unsorted_list,10)
	if len(sorted_list)<=10:
		print sorted_list



