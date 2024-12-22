import cv2
import imutils
image = cv2.imread('Noise_salt_and_pepper.png')

# median blur filter in openCv library
median_image = cv2.medianBlur(image, 3)
justify_image = cv2.convertScaleAbs(median_image, alpha=100 / 127.0, beta=20)
rotated_image = imutils.rotate(justify_image, 180)

cv2.imshow('Original', image)
cv2.imshow('Filtered', median_image)
cv2.imshow('Justified', justify_image)
cv2.imshow('Rotated', rotated_image)

cv2.waitKey(0)
