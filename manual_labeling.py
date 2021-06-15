import numpy as np
from tifffile import imread, imsave
import os

#1 for autofluorescence
#2 for neurons
path_r = r"C:\Users\lmorales-curiel\Documents\Watershed\done"
path_s = r"C:\Users\lmorales-curiel\Documents\Watershed\manual_label"
file = "contour_MSB661_AD4-40x_1.1-0000000_1_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))
img[img == 2] = 2
img[img >= 4] = 2
img[img == 1] = 1
img[img == 3] = 1

imsave(os.path.join(path_s, file), img)

file = "contour_MSB661_AD4-40x_1.1-0000000_6_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))

img[img == 2] = 100
img[img == 1] = 200
img[img == 3] = 1
img[img == 4] = 2
img[img == 5] = 2
img[img == 6] = 2
img[img == 7] = 2
img[img == 8] = 1
img[img == 100] = 1
img[img >= 9] = 2

imsave(os.path.join(path_s, file), img)


file = "contour_MSB661_AD4-40x_1.1-0000000_8_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))
img[img == 1] = 2
img[img == 23] = 1
img[img == 21] = 1
img[img == 22] = 1
img[img == 20] = 1
img[img > 1] = 2
imsave(os.path.join(path_s, file), img)


file = "contour_MSB661_AD4-40x_1.1-0000000_12_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))
img[img == 1] = 100
img[img == 25] = 1
img[img == 24] = 1
img[img == 23] = 1
img[img == 22] = 1
img[img == 21] = 1
img[img == 20] = 1
img[img == 10] = 1
img[img == 6] = 1
img[img == 4] = 1
img[img == 3] = 1
img[img == 2] = 1
img[img > 1] = 2
imsave(os.path.join(path_s, file), img)


file = "contour_MSB661_AD4-40x_1.1-0000000_24_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))
img[img == 2] = 1
img[img == 19] = 2
img[img == 17] = 2
img[img == 16] = 2
img[img == 14] = 2
img[img == 13] = 2
img[img == 12] = 2
img[img == 11] = 2
img[img == 10] = 2
img[img == 9] = 2
img[img == 5] = 2
img[img == 4] = 2
img[img == 3] = 2

img[img > 3] = 1

imsave(os.path.join(path_s, file), img)

file = "contour_MSB661_AD4-40x_1.1-0000000_26_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))
img[img == 2] = 1
img[img == 22] = 2
img[img == 12] = 2
img[img == 10] = 2
img[img == 11] = 2
img[img == 13] = 2
img[img == 15] = 2
img[img == 16] = 2
img[img == 9] = 2

img[img == 1] = 1
img[img == 3] = 1

img[img > 3] = 1

imsave(os.path.join(path_s, file), img)


file = "contour_MSB661_AD4-40x_1.1-0000000_27_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))

img[img == 23] = 1
img[img == 24] = 1
img[img == 8] = 1
img[img == 22] = 1
img[img == 7] = 1
img[img == 1] = 1
img[img == 2] = 1
img[img == 3] = 1
img[img == 4] = 1
img[img == 6] = 1
img[img == 9] = 1
img[img == 5] = 1
img[img > 1] = 2

imsave(os.path.join(path_s, file), img)



file = "contour_MSB661_AD4-40x_1.1-0000000_31_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))

img[img == 1] = 100
img[img == 9] = 1
img[img == 13] = 1
img[img == 15] = 1
img[img == 20] = 1
img[img == 22] = 1
img[img == 18] = 1
img[img == 16] = 1
img[img == 19] = 1
img[img == 24] = 1
img[img == 26] = 1

img[img > 1] = 2

imsave(os.path.join(path_s, file), img)


file = "contour_MSB661_AD4-40x_1.1-0000000_33_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))

img[img == 14] = 1
img[img == 6] = 1
img[img == 1] = 1
img[img == 5] = 1

img[img > 1] = 2

imsave(os.path.join(path_s, file), img)


file = "contour_MSB661_AD4-40x_1.1-0000000_35_MMStack_Default.ome.tif"
img = imread(os.path.join(path_r, file))
img[img == 1] = 100
img[img == 20] = 1
img[img == 22] = 1
img[img == 16] = 1
img[img == 17] = 1
img[img == 19] = 1
img[img == 21] = 1
img[img == 23] = 1
img[img == 18] = 1

img[img > 1] = 2

imsave(os.path.join(path_s, file), img)
