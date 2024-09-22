import cv2
from mnist import MNIST
import numpy as np 
import matplotlib.pyplot as plt
#使用http://yann.lecun.com/exdb/mnist/ 官網之dataset。60000張traindata,10000張testdata,準確率94.78%。
#使用opencv knn module
trainnum=60000
testnum=10000
row=28#特徵影像的列數
col=28#特徵影像的行數
#images(list 資料)
#labels(array 資料)
mndata = MNIST()

trainimages, trainlabels = mndata.load_training()

testimages, testlabels = mndata.load_testing()

trainimages=np.asarray(trainimages).reshape((60000,28,28))
testimages=np.asarray(testimages).reshape((10000,28,28))
#print(trainimages.shape)
#print(trainimages)
#print(testimages.shape)
#print(testimages)

trainimages[trainimages>=122]=255
trainimages[trainimages<122]=0
testimages[testimages>=122]=255
testimages[testimages<122]=0

trainlabels=np.asarray(trainlabels).astype(np.int32)
testlabels=np.asarray(testlabels).astype(np.int32)

#提取樣本影像特徵
feature=np.zeros((trainnum,round(row/4),round(col/4)))#用來儲存所有樣本的特徵值
f=feature#簡化變數名稱
#print(f.shape) #看看特徵值的形狀是什麼樣子
for ni in range(0,trainnum):
	for nr in range(0,row):
		for nc in range(0,col):
			if trainimages[ni,nr,nc]==255:
				f[ni,int(nr/4),int(nc/4)]+=1
#將feature處理為單列形式
#reshape中-1那一項,會依照其他維度自動計算
train=f[:,:].reshape(-1,round(row/4)*round(col/4)).astype(np.float32)
#print(train.shape)

of=np.zeros((testnum,round(row/4),round(col/4)))#用來儲存待識別影像的特徵值

for ni in range(0,testnum):
	for nr in range(0,row):
		for nc in range(0,col):
			if testimages[ni,nr,nc]==255:
				of[ni,int(nr/4),int(nc/4)]+=1

test=of[:,:].reshape(-1,round(row/4)*round(col/4)).astype(np.float32)
#呼叫函數識別影像
#train 可以放traindata or train data feature
knn=cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,trainlabels)
ret, result, neighbours, dist = knn.findNearest(test, 11)
matches = result.reshape(-1)==testlabels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size

print("測試資料可以判斷為類型:\n", result)
print("距離目前點最近的11個鄰居是:\n", neighbours)
print("11個最近鄰居的距離:\n", dist)
print("accuracy:{}%".format(accuracy))
