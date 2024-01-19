import numpy as np
import matplotlib.pyplot as plt

array = np.random.normal(0,5,10000)
x=range(1,10001,1)

#散点图
plt.scatter(x,array)
plt.show()

#柱状图
for i in range(10000):
    plt.bar(x[i],array[i],color='b')
plt.show()

#折线图
plt.plot(x,array)
plt.show()