#!/usr/bin/env python

from bubblesort import bubbltsort
from insertionsort import insertionsort
from quicksort import quicksort
from lib_lab4 import *

def print_SSE(SSE_name, SSE):
	if (SSE < 1e-10):
		print SSE_name + ' =', SSE, 'passed'
	else:
		print SSE_name + ' =', SSE, 'failed'

if __name__ == '__main__':

	len_list = input('length of list = ')

	
	#generate a list
	unsorted_list = generateRandomNum(len_list)

	(SSE_bubble, result_test, result_ref) 	 = SSE_check(bubbltsort, sorted, unsorted_list)
	print_SSE('SSE_bubble   ', SSE_bubble)
	(SSE_quick, result_test, result_ref) 	 = SSE_check(quicksort, sorted, unsorted_list)
	print_SSE('SSE_quick    ', SSE_quick)
	(SSE_insertion, result_test, result_ref) = SSE_check(insertionsort, sorted, unsorted_list)
	print_SSE('SSE_insertion', SSE_insertion)
