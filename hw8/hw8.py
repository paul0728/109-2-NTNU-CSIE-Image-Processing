import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def count_elements(seq) -> dict:
  hist = {}
  for i in seq:
    hist[i] = hist.get(i, 0) + 1
  return hist

def draw_histogram(img):
  count= pd.Series(img.flatten())
  count.plot.hist(grid=True, bins=20, rwidth=0.9,
  color='#607c8e')
  plt.title('Histogram of bacteria')
  plt.xlabel('Counts')
  plt.ylabel('Gray scale')
  plt.grid(axis='y', alpha=0.75)
  plt.savefig("Histogram of bacteria.jpg")
  plt.show()

def calculate_t(counted):
  p=[]
  for i in range(256):
    if i not in counted.keys():
      counted[i]=0
  for i in counted.values():
    p.append(i/163000)
  result=[0]*256
  for t in range(256):
    a=0
    b=0
    m=0
    ma=0
    for i in range(t+1):
      a=a+p[i]
      ma=ma+i*p[i]
    for i in range(t+1,256):
      b=b+p[i]
    try:
      for i in range(256):
        m=m+i*p[i]
        result[t]=((ma-m*a)**2)/(a*b)
    except ZeroDivisionError:
        result[t]=0
  t=result.index(max(result))
  return t

def thresholding(img,t):

  '''
  for i in range(np.size(img,0)):
    for j in range(np.size(img,1)):
      if img[i,j]>=t:
        img[i,j]=255
      else: 
        img[i,j]=0
  '''
  img[img>=t]=255
  img[img<t]=0
  img = img.astype(np.uint8)
  retval=cv2.imwrite('bacteria_th.jpg',img)
  cv2.imshow('bacteria.jpg',img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
  img=cv2.imread('bacteria.jpg',cv2.IMREAD_GRAYSCALE)
  cv2.imshow('bacteria.jpg',img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  draw_histogram(img)
  thresholding(img,calculate_t(count_elements(sorted(img.flatten()))))
'''
  counted=count_elements(sorted(img.flatten()))
  t=calculate_t(counted)
  thresholding(img,t)
'''



