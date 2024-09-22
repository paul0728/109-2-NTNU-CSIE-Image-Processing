import cv2
import numpy as np

#讀圖片<class 'numpy.ndarray'>
img = cv2.imread('D:\\image_processing\\hw4\\miko_gray.jpg',cv2.IMREAD_GRAYSCALE)

# resize image
width = 676
height = 676
dim = (width, height)
img= cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
d_1= [[0,128,32,160],
    [192,64,224,96],
    [48,176,16,144],
    [240,112,208,80]]
d_2=[[0,56],[84,28]]
d1=[[0]*width for i in range(height)]
d2=[[0]*width for i in range(height)]

#產生D1
for i in range(int(height)):
  for j in range(int(width)):
    if i%4==0 and j%4==0:
      d1[i][j]=0
    if i%4==0 and j%4==1:
      d1[i][j]=128
    if i%4==0 and j%4==2:
      d1[i][j]=32
    if i%4==0 and j%4==3:
      d1[i][j]=160
    if i%4==1 and j%4==0:
      d1[i][j]=192
    if i%4==1 and j%4==1:
      d1[i][j]=64
    if i%4==1 and j%4==2:
      d1[i][j]=224
    if i%4==1 and j%4==3:
      d1[i][j]=96
    if i%4==2 and j%4==0:
      d1[i][j]=48
    if i%4==2 and j%4==1:
      d1[i][j]=176
    if i%4==2 and j%4==2:
      d1[i][j]=16
    if i%4==2 and j%4==3:
      d1[i][j]=144
    if i%4==3 and j%4==0:
      d1[i][j]=240
    if i%4==3 and j%4==1:
      d1[i][j]=112
    if i%4==3 and j%4==2:
      d1[i][j]=208
    if i%4==3 and j%4==3:
      d1[i][j]=80
#產生D2
for i in range(int(height)):
  for j in range(int(width)):
    if i%2==0 and j%2==0:
      d2[i][j]=0
    if i%2==0 and j%2==1:
      d2[i][j]=56
    if i%2==1 and j%2==0:
      d2[i][j]=84
    if i%2==1 and j%2==1:
      d2[i][j]=28
 



#Threshold image I
I1=[[0]*width for i in range(height)]
I2=[[0]*width for i in range(height)]
Q=[[0]*width for i in range(height)]

for i in range(height):
  for j in range(width):
    Q[i][j]=img[i,j]/85

for i in range(height):
  for j in range(width):
    if img[i,j]>d1[i][j]:
      I1[i][j]=255
    else:
      I1[i][j]=0

for i in range(height):
  for j in range(width):
    if (img[i,j]-85*Q[i][j])>d2[i][j]:
      I2[i][j]=Q[i][j]+1
    else:
      I2[i][j]=Q[i][j]+0
I1=np.array(I1,dtype=np.uint8)
I2=np.array(I2,dtype=np.uint8)
#print("I1=",I1)
#print("I2=",I2*64)
cv2.imshow('img',img)
cv2.imshow('I1',I1)
cv2.imshow('I2',I2*64)
retval1=cv2.imwrite('C:\\Users\\paul\\Desktop\\I1.jpg',I1)
retval2=cv2.imwrite('C:\\Users\\paul\\Desktop\\I2.jpg',I2*64)
cv2.waitKey(0)
cv2.destroyAllWindows()
