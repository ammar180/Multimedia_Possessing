import cv2
import numpy as np

def encode(data):
    if not data:
        return []
    result = []
    prev = data[0]
    count = 1
    for ch in data[1:]:
        if ch == prev:
            count += 1
        else:
            result.extend([prev,count])
            prev = ch
            count = 1

    result.extend([prev,count])
    return result

# read image in grayscale 2D (one chanel) as 8-bit to less size
img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# try to decrease image space by resizing
resized_image = cv2.resize(img, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# convert 2D image as 1D list with 'flatten', from numby
pixels = resized_image.flatten()
# complress rle algorithem encoding
compressed_data = encode(pixels)
print(compressed_data)
# save image as npy extention formate + with numpy array data type 16 bit
np.save("compressed_image2.npy", np.array(compressed_data, dtype=np.uint16))
