#!/usr/bin/env python

from complex import *
import math
import numpy as np


def roots(a, b, c):

	delta = (b ** 2.) - (4. * a * c)
	if delta > 0: # 2 different roots
		return [((-b)+math.sqrt(delta))/(2*a), ((-b)-math.sqrt(delta))/(2*a)], []
	elif delta == 0: # 1 root
		return [(-b)/(2.*a), (-b)/(2.*a)], []
	else : # 2 complex roots2
		re = (-b)/(2.*a)
		im = math.sqrt(-delta)/(2.*a)
		ans = Complex(re, im)
		return [],[(ans), (~ans)]

def check_roots(root_fun, a, b, c ):
	real_c_rts, complex_c_rts = root_fun(a,b,c)



	if len(real_c_rts) == 0:
		real_rts = sorted([rt.re for rt in complex_c_rts])
		imag_rts = sorted([rt.im for rt in complex_c_rts])
	else:
		real_rts = sorted([rt for rt in real_c_rts])
		imag_rts = sorted([0 for rt in real_c_rts])

	#print real_rts
	#print imag_rts

	np_rts = np.roots([a, b, c])

	print 'numpy results:', np_rts
	imag_np_rts = sorted(np_rts.imag)
	real_np_rts = sorted(np_rts.real)

	#print real_np_rts
	#print imag_np_rts

	try: 
		result = 'PASS'
		for i in xrange(len(real_rts)):
			if abs(real_rts[i] - real_np_rts[i]) > 1e-5:
				result = 'FAIL'
			if abs(imag_rts[i] - imag_np_rts[i]) > 1e-5:
				result = 'FAIL'
		print result

	except: 
		'deminsion error'
	


	

if __name__ == '__main__':

	a = input('a =')
	b = input('b =')
	c = input('c =')

	real_rts, complex_rts = roots(a,b,c)
	
	print''

	print len(real_rts), 'real roots :'
	for rt in real_rts:
		print ' ', rt

	print len(complex_rts), 'complex roots :'
	for rt in complex_rts:
		print ' ', rt
	print''

	check_roots(roots, a,b,c)