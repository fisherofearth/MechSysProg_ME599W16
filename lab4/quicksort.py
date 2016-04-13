#!/usr/bin/env python
from lib_lab4 import *

def quicksort(L):
	if len(L) <= 1: 
		return L
	sorted_list = quicksort([ sl for sl in L[1:] if sl < L[0]])  +  [ L[0] ]  +  quicksort( [ ll for ll in L[1:] if ll >= L[0] ] )
	return sorted_list


if __name__ == '__main__':
	len_list = input('length of list = ')

	#generate a list
	unsorted_list = generateRandomNum(len_list)

	sorted_list = quicksort(unsorted_list) 

	#print unsorted_list
	#print sorted_list
	print average_timer(quicksort,unsorted_list,10), 'sec'
	if len(sorted_list)<=10:
		print sorted_list