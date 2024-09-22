import cv2
import pandas as pd
import rgbtohsi_2
import numpy as np
import math
def he_i(img):
  row=img.shape[0]
  col=img.shape[1]
  for i in range(row):
    for j in range(col):
      if img[i,j]==0:
        img[i,j]=round((15/row*col)*sumn[0])
      elif img[i,j]==1:
        img[i,j]=round((15/row*col)*sumn[1])
      elif img[i,j]==2:
        img[i,j]=round((15/row*col)*sumn[2])
      elif img[i,j]==3:
        img[i,j]=round((15/row*col)*sumn[3])
      elif img[i,j]==4:
        img[i,j]=round((15/row*col)*sumn[4])
      elif img[i,j]==5:
        img[i,j]=round((15/row*col)*sumn[5])
      elif img[i,j]==6:
        img[i,j]=round((15/row*col)*sumn[6])
      elif img[i,j]==7:
        img[i,j]=round((15/row*col)*sumn[7])
      elif img[i,j]==8:
        img[i,j]=round((15/row*col)*sumn[8])
      elif img[i,j]==9:
        img[i,j]=round((15/row*col)*sumn[9])
      elif img[i,j]==10:
        img[i,j]=round((15/row*col)*sumn[10])
      elif img[i,j]==11:
        img[i,j]=round((15/row*col)*sumn[11])
      elif img[i,j]==12:
        img[i,j]=round((15/row*col)*sumn[12])
      elif img[i,j]==13:
        img[i,j]=round((15/row*col)*sumn[13])
      elif img[i,j]==14:
        img[i,j]=round((15/row*col)*sumn[14])
      elif img[i,j]==15:
        img[i,j]=round((15/row*col)*sumn[15])
      else:
       break
  img=img*16
  return img

n=[]
sumn=[0]*16
img = cv2.imread('miko.jpg')
hsi = rgbtohsi_2.rgbtohsi(img)
hsi1=(hsi[:,:,2]/16).astype(int)
hsi2=pd.Series(hsi1.flatten())

for i in hsi2.value_counts().sort_index():
  n.append(i)

for i in range(16):
  for j in range(i+1):
    sumn[i]+=n[j]

hsi[:,:,2]=he_i(hsi1)
output=rgbtohsi_2.hsitorgb(hsi)
output = output.astype(np.uint8)
cv2.imshow('input',img)
retval=cv2.imwrite('output.jpg',output)
cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()