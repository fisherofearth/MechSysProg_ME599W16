#!/usr/bin/env python

import matplotlib.pyplot as plt
from filter import mean_filter 

from intensity import IntensityRecorder



if __name__ == '__main__':
	filter_wd = 5	

	ir = IntensityRecorder()

	(data, st, et, T) = ir.read_data('Mon Feb 22 15:33:47 2016_to_Mon Feb 22 15:34:07 2016')

	print 'number of data =', len(data)
	print st, et, T

	filtered_data = mean_filter(data, filter_wd)
	dts = ir.daytime(filtered_data, 90)
	a = max(data) * 1#1.05
	b = min(data) * 1#0.95
	dts = [(dt * (a - b) + b) for dt in dts]

	X = [x*T for x in range(len(data))]

	# plot
	plt.figure(1)
	plt.plot(X, data, 'b-', label='raw data')
	plt.plot(X, filtered_data, 'r-', label='filtered data')
	plt.plot(X, dts, 'g-', label='daytime')

	plt.title('mu wabcam average intensity (start from ' + st + ')')
	plt.xlabel('second')
	plt.ylabel('average intensity')
	plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)

	plt.show()
	
