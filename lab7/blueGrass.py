#!/usr/bin/env python

from grabber import Webcam

from PIL import Image as Img
import numpy as np
import time

BLUE = (0, 0, 255)


class BlueGrass:
	def __init__(self):
		self.mask = Img.open('mask2.jpg')
		


	def convert_lightBlue(self, filename):
		try:
			#self.img = Img.open(filename)
			self.img = Webcam().grab_image()
			self.img_new = self.img.copy()

			pix_img = self.img_new.load()
			pix_mask = self.mask.load()

			time_start = time.time()
			for x in xrange(self.img_new.size[0]):
				for y in xrange(self.img_new.size[1]):
					if (pix_mask[x, y][0]) > 250:
						if(pix_img[x, y][1] > (pix_img[x, y][0]-0)) and (pix_img[x, y][1] > (pix_img[x, y][2]-0)):
							pix_img[x, y] = BLUE
			time_end = time.time()
			print (time_end - time_start)
			return self.img_new
		except:
			print 'error'
			exit()

	def convert_nature(self, filename):
		
		#self.img = Img.open(filename)
		self.img = Webcam().grab_image()
		self.img_new = self.img.copy()

		pix_img_new = self.img_new.load()
		pix_mask = self.mask.load()

		time_start = time.time()
		for x in xrange(self.img_new.size[0]):
			for y in xrange(self.img_new.size[1]):
				if (pix_mask[x, y][0]) > 250:
					if(pix_img_new[x, y][1] > (pix_img_new[x, y][0]-20)) and (pix_img_new[x, y][1] > (pix_img_new[x, y][2]-20)):
						pix_img_new[x, y] = (int(pix_img_new[x,y][2]*0.8), int(pix_img_new[x,y][0]*0.8), pix_img_new[x,y][1])

		time_end = time.time()
		print (time_end - time_start)
		return self.img_new
	


if __name__ == '__main__':

	bs = BlueGrass()
	bs.convert_lightBlue('11.jpg').show()
	bs.convert_nature('11.jpg').show()
