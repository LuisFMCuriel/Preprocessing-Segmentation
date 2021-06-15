import cv2
import numpy as np
from tifffile import imread, imsave


def watershed(image):
	image -= int(np.amax(image)*0.05)
	image = image = np.clip(image, 0.0, 255.0)
	img = np.zeros((image.shape[0], image.shape[1], 3))
	frame = np.zeros_like(image[:,:])
	img[:,:,0] = image[:,:]
	img[:,:,1] = frame
	img[:,:,2] = frame

	img = img.astype(np.uint8)
	#img = GT[0,:,:].astype(np.uint8)

	ret, thresh = cv2.threshold(image.astype(np.uint8),0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


	# noise removal
	kernel = np.ones((3,3),np.uint8)
	opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
	# sure background area
	sure_bg = cv2.dilate(opening,kernel,iterations=3)
	# Finding sure foreground area
	dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
	ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
	# Finding unknown region
	sure_fg = np.uint8(sure_fg)
	unknown = cv2.subtract(sure_bg,sure_fg)


	# Marker labelling
	ret, markers = cv2.connectedComponents(sure_fg)
	# Add one to all labels so that sure background is not 0, but 1
	markers = markers+1
	# Now, mark the region of unknown with zero
	markers[unknown==255] = 0

	markers = cv2.watershed(img,markers)
	img[markers == 2] = [0,0,0]
	img[markers == 0] = [0,0,0]
	img[markers == 1] = [255,255,255]
	img[markers == 3] = [0,0,0]
	img[markers == -1] = [0,0,0]
	return markers, img[:,:,0]
