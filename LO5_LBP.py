import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern
from skimage import data
import numpy as np

image = data.camera()

radius = 1
n_points = 8 * radius

lbp = local_binary_pattern(image, n_points, radius, method='uniform')

lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2))

lbp_hist = lbp_hist.astype(float)
lbp_hist /= (lbp_hist.sum() + 1e-6)

fig, (axes1, axes2)= plt.subplots(1, 2, figsize=(12, 6))

# show original image
axes1.imshow(image, cmap='gray')
axes1.set_title('Original Image')
axes1.axis('Off')

# show LBP image
axes2.imshow(lbp, cmap='gray')
axes2.set_title('LBP Image')
axes2.axis('Off')

plt.figure(figsize=(8, 6))
plt.bar(np.arange(0, len(lbp_hist)), lbp_hist, color='blue')
plt.title("Local Binary Patterns")
plt.xlabel("LBP Prototype")
plt.ylabel("% of Picxels")
plt.show()