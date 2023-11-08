import cv2
import numpy as np


# Calculates the error between two images of same size. low error = more equal
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse


# Resizes the bigger image into the smaller image
def same_size(img1, img2):
    h, w = img1.shape
    h2, w2 = img2.shape
    if h * w >= h2 * w2:
        img1 = cv2.resize(img1, (w2, h2))
    else:
        img2 = cv2.resize(img2, (w, h))
    return img1, img2


# Compares the image with every image saved
def compare_imgs(img_spot, n):
    img_spot_gray = cv2.cvtColor(img_spot, cv2.COLOR_BGR2GRAY)

    error = 100

    for i in range(n):
        img_to_compare = cv2.imread(f'spots_detected/img_spot{i}.jpeg')
        img_to_compare_gray = cv2.cvtColor(img_to_compare, cv2.COLOR_BGR2GRAY)

        # If the size of the two images are similar
        if (abs(img_to_compare.shape[0] - img_spot_gray.shape[0])<=15) & (abs(img_to_compare.shape[1] - img_spot_gray.shape[1])<=15):
            img_to_compare_gray, img_spot_gray = same_size(img_to_compare_gray, img_spot_gray)
            error = mse(img_to_compare_gray, img_spot_gray)
            if error <= 25: 
                break

    return error