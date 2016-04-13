#!/usr/bin/env python


from PIL import Image 
from grabber import Webcam
import time
import math
import numpy as np

def distance(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2. + (p1[1]-p2[1])**2. + (p1[2]-p2[2])**2.)

def construct_diff_img(img_diff, data):
	data_int = [int(d) for d in data]
	img_diff.putdata([tuple([d,d,d]) for d in data_int],1, 0)
	return img_dif

if __name__ == '__main__':
	threshold = 9
	webcam = Webcam()
	
	image1 = webcam.grab_image()
	sx,sy = image1.size
	sx = sx/2
	sy = sy/2
	box = (sx-300, sy-50, sx+100, sy+100)
	#box = (0,0,sx,sy)
	image1 = image1.crop(box)

	for i in xrange(100):
		
		time.sleep(1)
		image2 = webcam.grab_image().crop(box)

	 	#image1 = Image.open('image1')
	 	#image2 = Image.open('image2')

	 	#img_diff = Image.new(image1.mode, image1.size, "black")

	 	#image1.show()
	 	#image2.show()

	 	d_im1 = image1.getdata()
	 	d_im2 = image2.getdata()

	 	d_diff = [distance(d1, d2) for d1, d2 in zip(d_im1, d_im2)]
	 	
	 	ref = np.mean(d_diff)
	 	if ref < threshold:
	 		moving = False
	 	else:
	 		moving = True
	 	print ref, moving

	 	#construct_diff_img(img_diff, d_diff)
	 	#img_diff.show()
	 	image1 = image2