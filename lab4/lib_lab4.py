#!/usr/bin/env python

import time
from random import random


def average_timer(fun, listName, times_run):
	start = time.time()
	for i in xrange(times_run):
		fun(listName)
	end = time. time()
	return (end - start) / times_run

def generateRandomNum(length):
	return [random() for i in xrange(length)]

#def generateRandomInt(length):
#	return [random.randint(1, 100) for i in xrange(length)]

def SSE_check(fun_test, fun_ref, data):
	result_test = fun_test(data)
	result_ref = fun_ref(data)
	SSE = sum([(result_test[i] - result_ref[i])**2 for i in xrange(len(data))])
	return SSE, result_test, result_ref

