import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




def plot_he_gray(img,name):
  img=(img/16).astype(int)
  for i in range(675):
    for j in range(675):
      if img[i,j]==0:
        img[i,j]=round((15/455625)*sumn[0])
      elif img[i,j]==1:
        img[i,j]=round((15/455625)*sumn[1])
      elif img[i,j]==2:
        img[i,j]=round((15/455625)*sumn[2])
      elif img[i,j]==3:
        img[i,j]=round((15/455625)*sumn[3])
      elif img[i,j]==4:
        img[i,j]=round((15/455625)*sumn[4])
      elif img[i,j]==5:
        img[i,j]=round((15/455625)*sumn[5])
      elif img[i,j]==6:
        img[i,j]=round((15/455625)*sumn[6])
      elif img[i,j]==7:
        img[i,j]=round((15/455625)*sumn[7])
      elif img[i,j]==8:
        img[i,j]=round((15/455625)*sumn[8])
      elif img[i,j]==9:
        img[i,j]=round((15/455625)*sumn[9])
      elif img[i,j]==10:
        img[i,j]=round((15/455625)*sumn[10])
      elif img[i,j]==11:
        img[i,j]=round((15/455625)*sumn[11])
      elif img[i,j]==12:
        img[i,j]=round((15/455625)*sumn[12])
      elif img[i,j]==13:
        img[i,j]=round((15/455625)*sumn[13])
      elif img[i,j]==14:
        img[i,j]=round((15/455625)*sumn[14])
      elif img[i,j]==15:
        img[i,j]=round((15/455625)*sumn[15])
      else:
       break
  img = img.astype(np.uint8)
  cv2.imshow(name,img*16)
  cv2.waitKey(0)
  retval=cv2.imwrite(name,img*16)

def plot_he_color(gray,img,name):
  o=gray
  gray=(gray/16).astype(int)
  for i in range(675):
    for j in range(675):
      if gray[i,j]==0:
        gray[i,j]=round((15/455625)*sumn[0])
      elif gray[i,j]==1:
        gray[i,j]=round((15/455625)*sumn[1])
      elif gray[i,j]==2:
        gray[i,j]=round((15/455625)*sumn[2])
      elif gray[i,j]==3:
        gray[i,j]=round((15/455625)*sumn[3])
      elif gray[i,j]==4:
        gray[i,j]=round((15/455625)*sumn[4])
      elif gray[i,j]==5:
        gray[i,j]=round((15/455625)*sumn[5])
      elif gray[i,j]==6:
        gray[i,j]=round((15/455625)*sumn[6])
      elif gray[i,j]==7:
        gray[i,j]=round((15/455625)*sumn[7])
      elif gray[i,j]==8:
        gray[i,j]=round((15/455625)*sumn[8])
      elif gray[i,j]==9:
        gray[i,j]=round((15/455625)*sumn[9])
      elif gray[i,j]==10:
        gray[i,j]=round((15/455625)*sumn[10])
      elif gray[i,j]==11:
        gray[i,j]=round((15/455625)*sumn[11])
      elif gray[i,j]==12:
        gray[i,j]=round((15/455625)*sumn[12])
      elif gray[i,j]==13:
        gray[i,j]=round((15/455625)*sumn[13])
      elif gray[i,j]==14:
        gray[i,j]=round((15/455625)*sumn[14])
      elif gray[i,j]==15:
        gray[i,j]=round((15/455625)*sumn[15])
      else:
       break
  r=(gray*16)/(o+0.0000000000000001)
  for k in range(3):
    img[:,:,k]=img[:,:,k]*r
  img = img.astype(np.uint8)

  #miko.jpg HE後之Histogram
  color = ('b','g','r')
  for i,col in enumerate(color):
      histr = cv2.calcHist([img],[i],None,[256],[0,256])
      plt.plot(histr,color = col)
      plt.xlim([0,256])
  plt.savefig("miko_color_he_histogram.jpg")
  plt.show()
  retval=cv2.imwrite(name,img)
  cv2.imshow(name,img)
  cv2.waitKey(0)

#照片轉成grayscale
def rgb2gray(rgb):
  return np.dot(rgb[..., :3],[0.2,0.5,0.3])




img1 = cv2.imread('miko.jpg')
img2 = cv2.imread('miko_gray.jpg',cv2.IMREAD_GRAYSCALE)
img1_plot=img1
img2_plot=img2
gray=rgb2gray(img1_plot)
#miko_gray.jpg HE前Histogram
L=16
T=455625
n=[]
rv=[0]*16
sumn=[0]*16
he2=[]
img2=(img2/16).astype(int)
img2=pd.Series(img2.flatten())
img2.plot.hist(grid=True, bins=20, rwidth=0.9,
color='#607c8e')
plt.title('miko_gray_histogram')
plt.xlabel('gray_level')
plt.ylabel('count')
plt.grid(axis='y', alpha=0.75)
plt.savefig("miko_gray_histogram.jpg")
plt.show()




#miko_gray.jpg HE後之Histogram
for i in img2.value_counts().sort_index():
  n.append(i)

for i in range(16):
  for j in range(i+1):
    sumn[i]+=n[j]



for i in range(16):
  rv[i]=round((15/455625)*sumn[i])
  he2.extend([rv[i]]*n[i])

#print(plot2)
he2=pd.Series(np.array(he2))
he2.plot.hist(grid=True, bins=20, rwidth=0.9,
color='#607c8e')
plt.title('miko_gray_he_histogram')
plt.xlabel('gray_level')
plt.ylabel('count')
plt.grid(axis='y', alpha=0.75)
plt.savefig("miko_gray_he_histogram.jpg")
plt.show()



#miko_gray.jpg HE後之output
plot_he_gray(img2_plot,"miko_gray_he.jpg")

#miko.jpg HE前之Histogram
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img1],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.savefig("miko_color_histogram.jpg")
plt.show()


#miko.jpg HE後之histogram和output
plot_he_color(gray,img1_plot,"miko_he.jpg")




