import cv2
import numpy as np

image = cv2.imread('sample.jpg')

# convert to hsv format
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# read chanels
hue_chanel = hsv_image[:,:,0]
saturation_chanel = hsv_image[:,:,1]
value_chanel = hsv_image[:,:,2]

# adjust chanels ->
# hue: max_180,
hue_chanel = (hue_chanel + 30) % 180
# saturation: max_300
saturation_chanel = (saturation_chanel + 30) % 300
# value: max_255
value_chanel = np.clip(value_chanel +10, 0, 255)


# reassign chanels
hsv_image[:,:,0] = hue_chanel
hsv_image[:,:,1] = saturation_chanel
hsv_image[:,:,2] = value_chanel

bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow('Original Image', image)
cv2.imshow('Modified Image', bgr_image)
cv2.waitKey(0)
