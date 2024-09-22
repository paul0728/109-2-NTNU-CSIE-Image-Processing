
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage.filters import median_filter
import numpy as np


def unsharp(image, sigma, strength):
    # Median filtering
    image_mf = median_filter(image, sigma)
    # Calculate the Laplacian
    lap = cv2.Laplacian(image_mf,cv2.CV_64F)
    # Calculate the sharpened image
    sharp = image-strength*lap
    # Saturate the pixels in either direction
    
    sharp[sharp>255] = 255
    sharp[sharp<0] = 0
    
    return sharp

img = plt.imread('miko.jpg')
sharp1 = np.zeros_like(img)
for i in range(3):
    sharp1[:,:,i] = unsharp(img[:,:,i], 5, 0.8)

#Average filter
blur = cv2.blur(img,(5,5))
#median filter
median = cv2.medianBlur(img,5)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur),plt.title('Average filter ')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(median),plt.title('median filter')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(sharp1),plt.title('Unsharp masking')
plt.xticks([]), plt.yticks([])
plt.savefig("miko_filter.jpg",)
plt.show()
