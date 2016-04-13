#!/usr/bin/env python

import math
import numpy as np

class Circle:
	def __init__(self, radius=1):
		self.radius = float(radius)

	def area(self):
		return (self.radius**2) * math.pi

	def diameter(self):
		return self.radius * 2.

	def corcumference(self):
		return self.radius * 2. *  math.pi


def CheckCircle(circle_class, radius = 1):
	diameter =  radius * 2.
	area = (radius**2) * math.pi
	corcumference = radius * 2. *  math.pi

	circle1 =  circle_class(radius = r)

	if abs(circle1.diameter() - diameter) < 1e-10:
		print 'diameter:', 'Pass'
	else:
		print 'diameter: ', 'Fail'
	
	if abs(circle1.area() - area) < 1e-10:
		print 'area:    ', 'Pass'
	else:
		print 'area:    ', 'Fail'

	if abs(circle1.corcumference() - corcumference) < 1e-10:
		print 'corcumference: ', 'Pass'
	else:
		print 'corcumference: ', 'Fail'


if __name__ == '__main__':

	r = input('radius =')
	circle1 =  Circle(radius = r)

	print 'radius        =', circle1.radius
	print 'diameter      =', circle1.diameter()
	print 'area          =', circle1.area()
	print 'corcumference =', circle1.corcumference()	

	print 'Checking ...'
	CheckCircle(Circle, radius = r)