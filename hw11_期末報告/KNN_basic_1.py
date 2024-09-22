import cv2
import numpy as np
import matplotlib.pyplot as plt
#用於訓練的資料
#rand1資料位於(0,30)
rand1 = np.random.randint(0, 30, (20, 2)).astype(np.float32)
#rand2資料位於(70,100)
rand2 = np.random.randint(70, 100, (20, 2)).astype(np.float32)
#將rand 1和rand 連接為訓練資料
trainData = np.vstack((rand1,rand2))
print("trainData=",trainData)
#資料標籤,共兩種:0和1
#r1Lanel對應著rand1標籤,為類型0
r1Label = np.zeros((20,1)).astype(np.float32)
#r2Lanel對應著rand2標籤,為類型1
r2Label = np.ones((20,1)).astype(np.float32)
tdLabel = np.vstack((r1Label,r2Label))
#使用綠色標記類型0
g = trainData[tdLabel.ravel()==0]
plt.scatter(g[:,0],g[:,1],20,'g','o')
#使用藍色標記類型1
b = trainData[tdLabel.ravel()==1]
plt.scatter(b[:,0],b[:,1],20,'b','s')
#plt.show
#test為用於測試的亂數,該數在0-100之間
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:,0],test[:,1],20,'r','*')
#呼叫opencv內的k近鄰模組,並進行訓練
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, tdLabel)
#使用k近鄰演算法分類
ret, result, neighbours, dist = knn.findNearest(test, 5)
#顯示處理結果
print("目前亂數可以判斷為類型:",result)
print("距離目前點最近的5個鄰居是:", neighbours)
print("5個最近鄰居的距離", dist)
#可觀察一下顯示,比較上述輸出
plt.show()
