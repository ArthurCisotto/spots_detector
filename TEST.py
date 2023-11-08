
import cv2

import numpy as np

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

img_compare = cv2.imread(f'teste/img_spot9.jpeg')
img_compare2 = cv2.imread(f'teste/img_spot2.jpeg')
img_compare = cv2.cvtColor(img_compare, cv2.COLOR_BGR2GRAY)
img_compare2 = cv2.cvtColor(img_compare2, cv2.COLOR_BGR2GRAY)

print(img_compare.shape, img_compare.shape[0] * img_compare.shape[1])
print(img_compare2.shape, img_compare2.shape[0] * img_compare2.shape[1])
print(img_compare.shape[0] - img_compare2.shape[0], img_compare.shape[1] - img_compare2.shape[1])


h,w = img_compare.shape
h2,w2 = img_compare2.shape

if h * w >= h2 * w2:
   img_compare = cv2.resize(img_compare, (w2, h2))
else:
   img_compare2 = cv2.resize(img_compare2, (w, h))

print(img_compare.shape, img_compare.shape[0] * img_compare.shape[1])
print(img_compare2.shape, img_compare2.shape[0] * img_compare2.shape[1])
error, diff = mse(img_compare, img_compare2)
print("Image matching Error between the two images:",error)