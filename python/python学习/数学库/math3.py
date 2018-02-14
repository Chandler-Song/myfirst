import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x =  mu + sigma * np.random.randn(10000)
plt.hist(x, 50, normed = 1, facecolor = 'g')#50绘制50个柱体，nomed总面积为1
plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60, 0.025, r"$\mu = 100,\ \sigma = 15$")#指定坐标显示文本
plt.axis([40, 160, 0, 0.03])#指定下xy轴形式
plt.show()