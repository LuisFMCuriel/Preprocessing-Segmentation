from watershed import watershed
import os
from tifffile import imread, imsave
import numpy as np
import cv2
import matplotlib.pyplot as plt

path_r = r"C:\Users\lmorales-curiel\Documents\Watershed\hyst"
path_s = r"C:\Users\lmorales-curiel\Documents\Watershed\hyst_done"
'''
for filename in os.listdir(path_r):
	img = imread(os.path.join(path_r, filename))
	img = img[0,int(img.shape[1]/2),:,:]
	imsave(os.path.join(path_s,filename), img)
'''


def contour(img):
	img = img.astype(np.uint8)
	ret, thresh = cv2.threshold(img, 127, 255, 0)
	print(thresh.shape)
	contours, hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for i,cont in enumerate(contours):
		#if len(cont) < 1300:
		thresh = cv2.drawContours(thresh, [cont], -1, i+1, -1)

	return thresh

#read all images
for i, filename in enumerate(os.listdir(path_r)):
	img = imread(os.path.join(path_r, filename))

	#Call watershed function
	marker, mask = watershed(img)

	#Get the contour of the mask so we can create segmentation classes
	contours = contour(mask)
	contours[contours > 200] = 0
	#Create the mask using contours
	binary = (contours > 0).astype(int)
	#apply the mask to the original image
	print(img.dtype)
	applied = img.astype(np.float32) * binary.astype(np.float32)
	
	#Save images
	imsave(os.path.join(path_s, "marker_"+filename), marker)
	imsave(os.path.join(path_s, "mask_"+filename), mask)
	imsave(os.path.join(path_s, "applied_"+filename), applied)
	imsave(os.path.join(path_s, "contour_"+filename), contours)
	imsave(os.path.join(path_s, "binary_"+filename), binary)
	print("Succesfully saved " + filename)

