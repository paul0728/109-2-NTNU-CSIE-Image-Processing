import cv2
from mnist import MNIST
import numpy as np 
import matplotlib.pyplot as plt
#使用http://yann.lecun.com/exdb/mnist/ 官網之dataset之testdata其中之8000張當作traindata,另外一張當testdata。無準確率計算。
#使用opencv knn module
#讀取樣本(特徵)影像的值
s=".\\train\\"
num=8000#共有的樣本數目
row=28#特徵影像的列數
col=28#特徵影像的行數
a=np.zeros((num,row,col))#用來儲存所有樣本的數值
#print(a.shape)

n=0#用來儲存目前影像的編號
for i in range(0,10):
	for j in range(0,800):
		a[n,:,:]=cv2.imread(s+str(i)+'_'+str(j)+".bmp",0)
		n=n+1
a[a>=122]=255
a[a<122]=0
#提取樣本影像特徵
feature=np.zeros((num,round(row/4),round(col/4)))#用來儲存所有樣本的特徵值
f=feature#簡化變數名稱
#print(f.shape) #看看特徵值的形狀是什麼樣子
for ni in range(0,num):
	for nr in range(0,row):
		for nc in range(0,col):
			if a[ni,nr,nc]==255:
				f[ni,int(nr/4),int(nc/4)]+=1
#將feature處理為單列形式
#reshape中-1那一項,會依照其他維度自動計算
train=f[:,:].reshape(-1,round(row/4)*round(col/4)).astype(np.float32)
#print(train.shape)'''

#貼標籤,要注意,是range(0,100)而非range(0,101)
trainLabels=[int(i/800) for i in range(0,8000)]
trainLabels=np.asarray(trainLabels)
#print(trainLabels.shape)
#print(trainLabels.dtype)
#trainLabels=trainLabels.reshape(-1,1)
#print(trainLabels) #列印測試看看標籤值
#讀取影像值
o=cv2.imread(".\\test\\7_778.bmp",0) #讀取待識別影像
o[o>=122]=255
o[o<122]=0
of=np.zeros((round(row/4),round(col/4))) #用來儲存待識別影像的特徵值

for nr in range(0,row):
	for nc in range(0,col):
		if o[nr,nc]==255:
			of[int(nr/4),int(nc/4)]+=1

test=of.reshape(-1,round(row/4)*round(col/4)).astype(np.float32)
#呼叫函數識別影像
#train 可以放traindata or train data feature
knn=cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,trainLabels)
ret, result, neighbours, dist = knn.findNearest(test, 11)
print("測試資料可以判斷為類型:",result)
print("距離目前點最近的11個鄰居是:", neighbours)
print("11個最近鄰居的距離", dist)

