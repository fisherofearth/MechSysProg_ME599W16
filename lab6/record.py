#!/usr/bin/env python

from intensity import IntensityRecorder


if __name__ == '__main__':

	time_sec = input('time =')
	T = 1

	intensityRecorder = IntensityRecorder(url='http://mu.webcam.oregonstate.edu')

	intensityRecorder.record(time_sec=time_sec, T=T)

	filename = '{0:}_to_{1:}'.format(intensityRecorder.start_time, intensityRecorder.end_time)
	intensityRecorder.save_data(filename)
	intensityRecorder.plot()
