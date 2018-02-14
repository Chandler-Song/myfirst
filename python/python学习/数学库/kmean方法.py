import numpy as np
import matplotlib.pyplot as plt

def initCenter(dataSet, k):
	numSamples, dim = dataSet.shape
	centers = np.zeros((k, dim))
	for i in range(k):
		index = int(np.random.uniform(0,numSamples))#随机生成0到numSample内一个数，可以指定个数
		centers[i, :] = dataSet[index, :]#二为
	print(centers)
	return centers

def Dist2Ceenters(sample, centers):
	k = centers.shape[0]
	dis2centers = np.zeros(k)
	for i in range(k):
		dis2centers[i] = np.sqrt(np.sum(np.power(sample - centers[i,:], 2)))
		return dis2centers
def Kmeans(dataSet, k, iterNum):
	numsamples = dataSet.shape[0]
	iterCount = 0

	clusterAssignment = np.zeros(numsamples)
	clusterChanged = True

	centers = initCenter(dataSet, k)
	while clusterChanged and iterCount < iterNum:
		clusterChanged = False
		iterCount = iterCount + 1
		for i in range(numsamples):
			dis2cent = Dist2Ceenters(dataSet[i, :], centers)
			minIndex = np.argmin(dis2cent)
			if clusterAssignment[i] != minIndex:
				clusterChanged = True
				clusterAssignment[i] = minIndex
		for j in range(k):
			pointersInCluster = dataSet[np.nonzero(clusterAssignment[:] == j)[0]]
			centers[j,:] = np.mean(pointersInCluster, axis = 0)
	print("Congratulation, Cluster Achieved!")
	return centers, clusterAssignment

def showCluster(dataSet, k, centers, clusterAssignment):
	numsamples, dim = dataSet.shape

	mark = ["or", "ob", "og", "om"]

	for i in range(numsamples):
		markIndex = int(clusterAssignment[i])
		plt.plot(dataSet[i,0],dataSet[i,1], mark[markIndex])

	for i in range(k):
		plt.plot(centers[i, 0], centers[i, 1],mark[i],markersize  = 17)

	plt.show()

def main():
	print("Step 1: loading data...")
	dataSet = []
	dataSetFile = open("./testSet.txt")
	for line in dataSetFile:
		lineArr = line.strip().split("\t")
		dataSet.append([float(lineArr[0]), float(lineArr[1])])

	print("Step 2: clustering...")
	dataSet = np.mat(dataSet)#转换为矩阵

	k = 4
	centers_result, clusterAssignment_result = Kmeans(dataSet, k, 100)

	print("step3: show the result...")
	showCluster(dataSet, k, centers_result, clusterAssignment_result)

main()