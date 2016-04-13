#!/usr/bin/env python

from grabber import Webcam
from PIL import Image as Img
import time
import math
import numpy as np
from PIL import ImageDraw
from numpy import random
from itertools import combinations
import ImageFilter
import scipy.io as sio
box = (0,20, 1024, 768)
thrshld= 40

def dist(p1, p2, T=0):
	d = math.sqrt((p1[0]-p2[0])**2. + (p1[1]-p2[1])**2. + (p1[2]-p2[2])**2.)
	if d < T:
		return (0, 0, 0)
	else:
		d = int(d)
		return (255, 255, 255)
def d_2p(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2. + (p1[1]-p2[1])**2.)


class PersonDetector:
	def __int__(self):
		pass

	def compute_differenct(self):
		a = 1
		live = True
		if live == True:
			image1 = Webcam().grab_image().crop(box)
			time.sleep(.5)
			image2 = Webcam().grab_image().crop(box)
		else:
			image1 = Img.open('1.jpg').crop(box)
			image2 = Img.open('2.jpg').crop(box)

		self.image_original1 = image1
		self.image_original2 = image2

		image1 = image1.filter(ImageFilter.Kernel(size=(3,3), kernel=(a,a,a,a,0,a,a,a,a)))
		image2 = image2.filter(ImageFilter.Kernel(size=(3,3), kernel=(a,a,a,a,0,a,a,a,a)))

		self.image_difference = Img.new('RGB', image1.size, 'black')
		pix_diff = self.image_difference.load()

		pix1 = image1.load()
		pix2 = image2.load()
		for x in xrange(image1.size[0]):
			for y in xrange(image1.size[1]):
				pix_diff[x,y] = dist(pix1[x,y], pix2[x,y], thrshld)


		self.image_difference = self.image_difference.filter(ImageFilter.BLUR)

		pix_diff = self.image_difference.load()
		for x in xrange(image1.size[0]):
			for y in xrange(image1.size[1]):
				if pix_diff[x,y][0] > thrshld:
					pix_diff[x,y] = (255, 255, 255)
				else:
					pix_diff[x,y] = (0, 0, 0)

		return self.image_difference


	def min_dist(self, centers, point):
		distances = [math.sqrt((point[0]-center[0])**2. + (point[1]-center[1])**2.) for center in centers]
		return np.argmin(distances)

	def recenter(self, cluster):
		if len(cluster) == 0:
			return (random.randint(low=0,high=1024), random.randint(low=0,high=768))
		else:
			c = np.mean(cluster, 0)
			return (int(c[0]), int(c[1]))

	def noise_filter(self):
		pass

	def k_mean(self, K = 2):
		mask = Img.open('mask5.jpg').crop(box)
		pix_mask = mask.load()

		pix_diff = self.image_difference.load()
		self.centers = [(random.randint(low=0,high=1024), random.randint(low=0,high=768)) for k in xrange(K)]
		points = []
		for x in xrange(box[2]-box[0]):
			for y in xrange(box[3]-box[1]):
				if pix_mask[x,y][0] < 100:
				 	pix_diff[x,y] = (0,0,0)
				elif pix_diff[x,y][0] > 0:
						points.append((x,y))


		for j in xrange(6):

			for i in xrange(15):
				clusters = [[] for k in xrange(K)]
				for p in points:
					g_idx = self.min_dist(self.centers, p)
					clusters[g_idx].append(p)
				self.centers = [self.recenter(cluster) for cluster in clusters]

			# delete cluster that is small or sparse
			c = 0
			del_idx = []
			for cluster in clusters:
				if len(cluster) < 80 or np.std(cluster) < 20:
					
					K -=1
					del_idx.append(c)
					for p in cluster:
						#pix_diff[p[0],p[1]] = (0,0,0)
						points.remove(p)
				c += 1
			for i in sorted(del_idx, reverse=True):
				del self.centers[i]

			# combine clusters that are close
		
			for com in xrange(5):
				idx_centers = combinations(range(len(self.centers)), 2)
				for idx in idx_centers:
					#print d_2p(self.centers[idx[0]], self.centers[idx[1]])
					if d_2p(self.centers[idx[0]], self.centers[idx[1]]) < 40: # if too close
						del self.centers[idx[1]]
						K -= 1
						break
		

		del_idx = []
		for c in xrange(len(clusters)):
			if len(clusters[c]) < 100:
				del_idx.append(c)
		for i in sorted(del_idx, reverse=True):
				del self.centers[i]
				del clusters[i]

		print '( x, y) , std, #ofPoint'
		for g in zip(self.centers, [int(np.std(cluster)) for cluster in clusters], [len(cluster) for cluster in clusters]):
			print g

		self.clusters = clusters
		#return locations

if __name__ == '__main__':
	pd = PersonDetector()
	#pd.compute_differenct().show()
	#pd.image_difference.save('diff5.jpg')

	pd.compute_differenct()
	#pd.image_difference = Img.open('diff1.jpg')
	pd.k_mean(K=50)

	
	draw = ImageDraw.Draw(pd.image_original1)
	for cnt, clts in zip(pd.centers, pd.clusters):

		
		#size1 = (c[0]-30, c[1]-40, c[0]+30, c[1]+40 )
		#size2 = (c[0]-20, c[1], c[0]+20, c[1]+20 )
		X = [clt[0] for clt in clts]
		Y = [clt[1] for clt in clts]
		size3 = (np.percentile(X, 25)-12,
			np.percentile(Y, 22)+8,
			np.percentile(X, 75)+12,
			np.percentile(Y, 80)+8
			)
		draw.ellipse(size3, outline=(255, 255, 0))
	del draw

	pd.image_original2.thumbnail((512,374),Img.ANTIALIAS)
	pd.image_difference.thumbnail((512,374),Img.ANTIALIAS)
	pd.image_original1.thumbnail((512,374),Img.ANTIALIAS)

	pd.image_original2.show()
	pd.image_difference.show()
	pd.image_original1.show()

	#pd.image_difference.filter(ImageFilter.BLUR).show()
	#pd.image_difference.filter(ImageFilter.MinFilter(1)).show()
	#a = 10
	#pd.image_difference.filter(ImageFilter.Kernel(size=(3,3), kernel=(a,a,a,a,a,a,a,a,a))).show()