#!/usr/bin/env python


from PIL import Image 
from grabber import Webcam
import time
import math
import numpy as np

def d(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2. + (p1[1]-p2[1])**2. + (p1[2]-p2[2])**2.)

def pick_constanct_pixel(p1,p2,p3):
	dist = [d(p1,p2), d(p2,p3), d(p3,p1)]

	d_min = dist[0]
	p_c = p1

	if dist[1] < d_min:
		d_min = dist[1]
		p_c = p2

	if dist[2] < d_min:
		d_min = dist[2]
		p_c = p3

	return p_c
	 

def remove_dyn(img1, img2, img3):
	img_diff = Image.new(img1.mode, img1.size, "black")

	constant_img = [pick_constanct_pixel(p1,p2,p3) for p1, p2, p3 in zip(img1.getdata(), img2.getdata(), img3.getdata())]


	img_diff.putdata(constant_img,1, 0)
	return img_diff

def photo_static(box):
	webcam = Webcam()
	image1 = webcam.grab_image().crop(box)
	time.sleep(1.5)
	image2 = webcam.grab_image().crop(box)
	time.sleep(1.5)
	image3 = webcam.grab_image().crop(box)

	#image1.show()
	#image2.show()
	#image3.show()

	return remove_dyn(image1, image2, image3)

if __name__ == '__main__':
	box = (222, 359, 522, 479)

	image_c = photo_static(box)

	image_c.show()
	image_c.save('image_c'+'.jpg', 'JPEG')
