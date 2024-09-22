import cv2
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def add_gaussian_noise(img, mean=0, sigma=math.sqrt(15)):
  global gaussian_out
  # 隨機生成高斯 noise (float + float)
  noise = np.random.normal(mean, sigma, img.shape)
  # noise + 原圖
  gaussian_out = img + noise
  # 所有值必須介於 0~1 之間，超過1 = 1，小於0 = 0
  gaussian_out = np.clip(gaussian_out, 0, 255)
  gaussian_out=np.uint8(gaussian_out)
  noise = np.uint8(noise)

  print("gaussian noise: ")
  cv2.imshow('noise',noise)
  cv2.waitKey(0)
  plot_histogram(gaussian_out)
  print("Picture add gaussian noise: ")
  cv2.imshow('gaussian_out',gaussian_out)
  cv2.waitKey(0)
#   return gaussian_out , noise



def plot_histogram(gaussian_out):
  gaussian_out=pd.Series(gaussian_out.flatten())
  gaussian_out.plot.hist(grid=True, bins=20, rwidth=0.9,
  color='#607c8e')
  plt.title('gaussian_out_histogram')
  plt.xlabel('gray_level')
  plt.ylabel('count')
  plt.grid(axis='y', alpha=0.75)
  plt.savefig("gaussian_out.jpg")
  plt.show()



img=np.array([[100]*500 for i in range(500)],dtype=np.uint8)
add_gaussian_noise(img)





