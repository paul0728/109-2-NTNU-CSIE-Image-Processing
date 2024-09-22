#ubyte轉成圖(1-D list)
from mnist import MNIST
import random

mndata = MNIST()

trainimages, trainlabels = mndata.load_training()
# or
testimages, testlabels = mndata.load_testing()

#image為長度為784之list(28*28照片)
print(len(trainimages))
#labels為長度為60000之array
print(len(trainlabels))
#image為長度為784之list(28*28照片)
print(len(testimages))
#labels為長度為10000之array
print(len(testlabels))
print(testlabels.size)



#index = random.randrange(0, len(testimages))  # choose an index ;-)
#print(mndata.display(trainimages[6000]))
#print(trainlabels)
#print(mndata.display(testimages[index]))