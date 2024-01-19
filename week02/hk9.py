#使用蒙特卡洛，计算区间[2,3]上定积分(x^2 + 4xsin(x))dx
import math
import numpy as np
def count(num,a,b):
    n = 0
    for i in range(1,num):
        x = np.random.uniform(a,b)
        y = np.random.uniform(0,25)
        y0 = x * x + 4 * x * math.sin(x)#随机取点与函数值进行比较
        if y<y0 :
            n += 1
    area = 25*(b-a)#计算投点范围的面积
    return (n*area/num)
a = 2
b = 3
num =10000000
print(count(num,a,b))

#进行验算
from scipy.integrate import quad
f = lambda x: x*x + 4*x*math.sin(x)
val,err = quad(f,2,3)
print(val)