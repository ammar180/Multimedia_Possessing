import cv2
from skimage.restoration import denoise_tv_chambolle
from skimage import data

image = data.camera()
lambda_reg = 0.9

tv_denoised_image = denoise_tv_chambolle(image, weight= lambda_reg)

cv2.imshow("Original", image)
cv2.imshow("tv_denoised_image", tv_denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
