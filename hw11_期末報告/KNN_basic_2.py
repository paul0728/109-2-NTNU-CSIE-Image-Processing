import cv2
import numpy as np
import matplotlib.pyplot as plt
# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
# Label each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)
# Take Red neighbours and plot them
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
# Take Blue neighbours and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')


#newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
#plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

# 10 new-comers
newcomers = np.random.randint(0,100,(10,2)).astype(np.float32)
plt.scatter(newcomers[:,0],newcomers[:,1],80,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results,neighbours,dist = knn.findNearest(newcomers, 5)
#ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)
# The results also will contain 10 labels.
print( "result:  {}\n".format(results) )
print( "neighbours:  {}\n".format(neighbours) )
print( "distance:  {}\n".format(dist) )
plt.show()

