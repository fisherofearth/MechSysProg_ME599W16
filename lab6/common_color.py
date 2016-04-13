#!/usr/bin/env python


from intensity import IntensityRecorder


if __name__ == '__main__':
	ir = IntensityRecorder(url='http://mu.webcam.oregonstate.edu')
	mccs = ir.most_commom_color()
	for mcc in mccs:
		print mcc