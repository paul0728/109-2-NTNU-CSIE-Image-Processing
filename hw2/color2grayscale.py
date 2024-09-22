# Load libraries
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#Define RGB to grayscale function
#I=(R+G+B)/3
def rgb2gray(rgb):
  return np.dot(rgb[..., :3],[0.2,0.5,0.3])
# Standard input image file name
img=mpimg.imread(sys.argv[1])
#Call RGB to grayscale function
gray=rgb2gray(img)
#Save output image file
#原圖
plt.imsave(sys.argv[1].split('.')[-2]+"_1"+sys.argv[1].split('.')[-1],img)
#灰階
plt.imsave(sys.argv[1].split('.')[-2]+"_gray."+sys.argv[1].split('.')[-1],gray,cmap='gray')

#Plot input and output images
figure,ax=plt.subplots(1,2)
ax[0].imshow(img)
ax[1].imshow(gray,cmap='gray')
plt.show()
