import cv2

# read photo as 8-bit grayscale image
grayscale_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
# convert image to rgp with chanels Red-0, Green-1, Blue-2
rgb_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2RGB)

# rgb_image[:,:, 0] = 0
# rgb_image[:,:, 1] = 0
# rgb_image[:,:, 2] = 0

resized_image = cv2.resize(grayscale_image, dsize=None, fx=1.5, fy=1.5)

cv2.imshow('8-bit Grayscale Image', grayscale_image)
# reshow image in BGR format (compatable with python)
cv2.imshow('Blue-Tinted 24-bit RGB Image' , cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR))
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
