import cv2
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def add_gaussian_noise(g,sigma=math.sqrt(15)):
  f=np.array([[100]*500 for i in range(500)],dtype=np.uint8)
  f1=np.array([[100]*500 for i in range(500)],dtype=np.uint8)
  for x in range(500):
    for y in range(0,500,2):
      r=0
      p=0
      while(r==0):
        r=random.uniform(0,1)
      while(p==0):
        p=random.uniform(0,1)
      z1=round(sigma*math.cos(2*math.pi*p)*math.sqrt(-2*math.log(r)))
      z2=round(sigma*math.sin(2*math.pi*p)*math.sqrt(-2*math.log(r)))
      f1[x,y]=g[x,y]+z1
      f1[x,y+1]=g[x,y+1]+z2

      if f1[x,y]<0:
        f[x,y]=0
      elif f1[x,y]>255:
        f[x,y]=255
      else:
        f[x,y]=f1[x,y]

      if f1[x,y+1]<0:
        f[x,y+1]=0
      elif f1[x,y+1]>255:
        f[x,y+1]=255
      else:
        f[x,y+1]=f1[x,y+1]
  plot_img('noisy_img.jpg',f)
  plot_histogram(f)
  

def plot_histogram(noisy_img):
  noisy_img=pd.Series(noisy_img.flatten())
  noisy_img.plot.hist(grid=True, bins=20, rwidth=0.9,
  color='#607c8e')
  plt.title('noisy_img_histogram')
  plt.xlabel('gray_level')
  plt.ylabel('count')
  plt.grid(axis='y', alpha=0.75)
  plt.savefig("noisy_img_histogram.jpg")
  plt.show()

def plot_img(filename,img):
  cv2.imshow(filename,img)
  cv2.waitKey(0)
  cv2.imwrite(filename,img)

img=np.array([[100]*500 for i in range(500)],dtype=np.uint8)
plot_img("original.jpg",img)
add_gaussian_noise(img)





