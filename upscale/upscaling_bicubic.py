import cv2

# Load the original image
original_image = cv2.imread('upscale/input.png')

# Upscale the image using linear interpolation
scaled_image = cv2.resize(original_image, (original_image.shape[1] * 4, original_image.shape[0] * 4), interpolation=cv2.INTER_CUBIC)

# Save the upscaled image
cv2.imwrite('upscale/upscaled_bicubic.jpeg', scaled_image)
