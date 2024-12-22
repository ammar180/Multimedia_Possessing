import cv2
import numpy as np

image = np.ones((400, 400, 3), dtype=np.uint8) * 255

start_point = (100,100)
end_point = (300, 100)
thickness = 6 
color = (0,255,255)

# cv2.line(image, start_point, end_point, color, thickness)
# cv2.circle(image, (200, 200), 100, color,thickness)
# cv2.rectangle(image, (100, 100), (300, 300), (0, 255, 0), 5)
# scaled_img = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

l1_xs, l1_ys = (10, 10)
l1_xe, l1_ye = (400, 400)

l2_xs, l2_ys = (100, 20)
l2_xe, l2_ye = (100, 400)

r_xs, r_ys = (50, 50)
r_xe, r_ye = (350, 350)

if r_xs > l1_xs: l1_xs = r_xs
if r_ys > l1_ys: l1_ys = r_ys

if r_xs > l2_xs: l2_xs = r_xs
if r_ys > l2_ys: l2_ys = r_ys

if r_xe < l1_xe: l1_xe = r_xe
if r_ye < l1_ye: l1_ye = r_ye

if r_ye < l2_ye: l2_ye = r_ye

cv2.line(image, (l1_xs,l1_ys), (l1_xe, l1_ye), (255,0,0), 5)
cv2.line(image, (l2_xs,l2_ys), (l2_xe, l2_ye), (0,0,255), 5)
cv2.rectangle(image, (r_xs, r_ys), (r_xe, r_ye), (0, 255, 0), 5)


cv2.imshow("shape", image)
cv2.waitKey(0)
cv2.destroyWindow("shape")
