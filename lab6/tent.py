#!/usr/bin/env python

from PIL import Image 
from grabber import Webcam
import time
import math
import numpy as np

from static import photo_static 

def dist(p1, p2):
	d = (math.sqrt((p1[0]-p2[0])**2. + (p1[1]-p2[1])**2. + (p1[2]-p2[2])**2.))
	if d > 100:
		return d
	else:
		return 0

def isTent(img_ref, img_live):
	
	img_diff = Image.new(img_ref.mode, img_ref.size, "black")
	data_diff = [int(dist(p1, p2)) for p1, p2 in zip(img_ref.getdata(), img_live.getdata())]
	img_diff.putdata([tuple([d,d,d]) for d in data_diff],1, 0)

	return img_diff


if __name__ == '__main__':
	threshold = 10

	webcam = Webcam()

	box = (222, 359, 522, 479)

	img_live = photo_static(box)
	img_live.show()

	img_ref = Image.open("ref1")
	img_ref.show()

	diff_img = isTent(img_ref, img_live)
	diff_img.show()

	#d_diff = [dist(d1, d2) for d1, d2 in zip(img_ref.getdata(), diff_img.getdata())]

 	ref = np.mean(diff_img.getdata())
 	if ref < threshold:
 		moving = False
 	else:
 		moving = True
 	print ref, moving