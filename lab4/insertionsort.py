#!/usr/bin/env python


# insertation sort

from lib_lab4 import *

def insertionsort(unsorted_list):
	sortedL=list(unsorted_list)
	for i in xrange(1,len(sortedL)):
		for j in xrange(i):
			if (sortedL[i]<sortedL[j]):
				(sortedL[i], sortedL[j]) = (sortedL[j], sortedL[i])
	return sortedL


if __name__ == '__main__':

	len_list = input('length of list = ')

	#generate a list
	unsorted_list = generateRandomNum(len_list)
	

	sorted_list = insertionsort(unsorted_list)

	#print unsorted_list
	
	
	if len(sorted_list)<=10:
		print sorted_list

	print average_timer(insertionsort,unsorted_list,10), 'sec'




