# https://www.hackersrealm.net/post/enhance-your-images-with-super-resolution-opencv

import cv2
from cv2 import dnn_superres

# initialize super resolution object
sr = dnn_superres.DnnSuperResImpl_create()

# read the model
path = 'upscale/EDSR_x4.pb'
sr.readModel(path)

# set the model and scale
sr.setModel('edsr', 4)

# load the image
image = cv2.imread('upscale/img_test3.png')

# upsample the image
upscaled = sr.upsample(image)

# save the upscaled image
cv2.imwrite('upscale/upscaled_EDSR.png', upscaled)