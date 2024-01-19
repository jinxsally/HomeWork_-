import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

array = np.random.normal(0,5,1000)
x=range(1,1001,1)

#散点图
sns.scatterplot(data=array)
plt.show()

#折线图
sns.lineplot(data=array)
plt.show()

#条形图
sns.histplot(array)
plt.show()