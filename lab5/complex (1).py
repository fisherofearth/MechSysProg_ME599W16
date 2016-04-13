#!/usr/bin/env python

class Complex:
	def __init__(self, real = 0.0, imaginary = 0.0):
		self.re = float(real)
		self.im = float(imaginary)

	def __str__(self):
		return '(' + str(self.re) + '{:+}'.format(self.im) + 'i' + ')'
		#retrun '{0:+} {1:+} i'.format(str(self.re), self.im) 

	def __add__(self, other):
		try:
			other = Complex(other)
		except:
			pass
		return Complex((self.re + other.re), (self.im + other.im))

	def __radd__(self, other):
		return self + other

	def __neg__(self):
		return Complex(-self.re, -self.im)

	def __sub__(self, other):
		return self + (-other)

	def __rsub__(self, other):
		return other + (-self)

	def __mul__(self, other):
		try:
			other = Complex(other)
		except:
			pass
		re = (self.re * other.re) - (self.im * other.im)
		im = (self.re * other.im) + (self.im * other.re)
		return Complex(re, im)

	def __rmul__(self, other):
		return self * other

	def __div__(self, other):
		try:
			other = Complex(other)
		except:
			pass
		rev = ~other#Complex(other.re, -other.im)
		num = self * rev
		den = (other.re ** 2.) + (other.im ** 2.)
		return Complex(num.re/den, num.im/den)

	def __rdiv__(self, other):
		return self / other

	def __invert__(self):
		return Complex(self.re, -self.im)



if __name__ == '__main__':


	print '-------------different inputs---------------'
	a = Complex(1.0, 2.3)    # 1 + 2.3i
	b = Complex(2)           # 1 + 0i
	c = Complex()            # 0 + 0i

	print 'a:', a
	print 'b:', b
	print 'c:', c

	print '--------------- __str__() ------------------'
	a = Complex(1, 2)
	b = Complex(1, -2)

	print 'a:', a
	print 'b:', b

	print '---------------- __add__() -----------------'
	a = Complex(1, 2)
	b = Complex(3, 4)
	print 'a + b :', a + b
	print 'a + 1 :', a + 1
	print '1 + a :', 1 + a

	print '---------------- __sub__() -----------------'
	a = Complex(1, 2)
	b = Complex(3, 4)
	print 'a - b :', a - b
	print 'a - 1 :', a - 1
	print '1 - a :', 1 - a

	print '---------------- __mul__() ------------------'
	a = Complex(5, 2)
	b = Complex(4, 3)
	print 'a x b =', a * b
	print 'a x 3 =', a * 3
	print '3 x a =', 3 * a	

	print '---------------- __div__() ------------------'
	a = Complex(2, -1)
	b = Complex(-3, 6)
	print 'a / b =', a / b
	print 'a / 3 =', a * 3
	print '3 / a =', 3 * a

	print '-------------- __invert__() -----------------'
	a = Complex(2, -1)
	print '~a =', ~a