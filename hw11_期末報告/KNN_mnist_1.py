import cv2
import numpy as np 
import matplotlib.pyplot as plt
#使用http://yann.lecun.com/exdb/mnist/ 官網之dataset之testdata其中之8000張當作traindata,另外一張當testdata。無準確率計算。
#完全手刻
#算出來之距離與使用opencv knn module算的不同,但預測結果相同

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
#print(feature.shape) #看看特徵值的形狀是什麼樣子
for ni in range(0,num):
	for nr in range(0,row):
		for nc in range(0,col):
			if a[ni,nr,nc]==255:
				feature[ni,int(nr/4),int(nc/4)]+=1
f=feature#簡化變數名稱


#####計算目前待識別影像的特徵值
o=cv2.imread(".\\test\\7_778.bmp",0) #讀取待識別影像
o[o>=122]=255
o[o<122]=0
of=np.zeros((round(row/4),round(col/4))) #用來儲存待識別影像的特徵值

for nr in range(0,row):
	for nc in range(0,col):
		if o[nr,nc]==255:
			of[int(nr/4),int(nc/4)]+=1


###開始計算,識別數字,計算鄰近的許多數字是多少,判斷結果
d=np.zeros(8000)
for i in range(8000):
	d[i]=np.sum((of-f[i,:,:])*(of-f[i,:,:]))
#print(d)
d=d.tolist()
d1=[]
neighbours=[]
Inf=max(d)
#print(Inf)
k=11
for i in range(k):
	neighbours.append(d.index(min(d)))
	d1.append(neighbours[i])
	d[d.index(min(d))]=Inf
#print(temp)  #看看都被識別為那些特徵值

neighbours=[int(i/800) for i in neighbours]
#也可以傳回去處理為array,是用函數處理
#temp=np.array(temp)
#temp=np.trunc(temp/10)
#print(temp)
#陣列r用來儲存結果,r[]表示k鄰近中'0'的個數,r[]表示k鄰近中'n'的個數
r=np.zeros(10)
for i in neighbours:
	r[int(i)]+=1
#print(r)

print("測試資料可以判斷為類型:"+str(np.argmax(r)))
print("距離目前點最近的11個鄰居是:", neighbours)
print("11個最近鄰居的距離", d1)


