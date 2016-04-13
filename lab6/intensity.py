#!/usr/bin/env python

from grabber import Webcam
import numpy as np
import matplotlib.pyplot as plt
import sched, time



class IntensityRecorder:
	def __init__(self, url = None):
		if url == None:
			self.webcam = Webcam()
		else:
			self.webcam = Webcam(url = url)
		self.averageIntensity = []

	def intensity(self, image):
		return np.mean(image)

	def capture_avg_intensity(self):
		self.averageIntensity.append(self.intensity(self.webcam.grab_image_data()))

	def record(self, time_sec, T):
		scheduler = sched.scheduler(time.time, time.sleep)
		for i in xrange((time_sec*T)):
			scheduler.enter(i*T, i, self.capture_avg_intensity, ())
			
		self.start_time = time.strftime("%c")
		print 'Start time =',self.start_time

		scheduler.run()

		self.end_time = time.strftime("%c")
		print 'End time =', self.end_time

	def plot(self):
		plt.figure(1)
		plt.plot(range(len(self.averageIntensity)), self.averageIntensity, label = 'intensity')
		plt.title('MU webcam average intensity, start from:' + self.start_time)
		plt.xlabel('second')
		plt.ylabel('average intensity')
		plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)
		plt.show()

	def save_data(self, filename):
		with open(filename, 'w') as f:
			f.write('start time : ' + self.start_time + '\n')
			f.write('end time   : ' + self.end_time + '\n')
			for i in xrange(len(self.averageIntensity)):
				f.write('{0}\t{1}\n'.format(i, self.averageIntensity[i]))
		

	def read_data(self, filename):
		data = []
		with open(filename, 'r') as f:
			start_time = f.readline().strip()
			end_time = f.readline().strip()
			T = float(f.readline().strip())
			for line in f:
				data.append(float([d for d in line.split()][1]))
		return data, start_time, end_time, T

	def daytime(self, intensity, threshold):
		dt = []
		if intensity[0] > threshold:
			isDayTime = True
		else:
			isDayTime = False

		for i in intensity:
			if i > threshold+5:
				isDayTime = True
			elif i <(threshold-5):
				isDayTime = False
			dt.append(isDayTime)
		return dt

	def most_commom_color(self, number = 10):
		image = self.webcam.grab_image_data()
		self.colors = {}
		for color in image:
			try:
				self.colors[color] += 1
			except:
				self.colors[color] = 1

		sorted_colors = sorted(self.colors.items(),key=lambda x: x[1],reverse=True)

		results = sorted_colors[:number]
		den = float(len(image))

		return [[c[0], c[1]/den] for c in results]

if __name__ == '__main__':
	
	ir = IntensityRecorder()
	ir.capture_avg_intensity()
	print ir.averageIntensity