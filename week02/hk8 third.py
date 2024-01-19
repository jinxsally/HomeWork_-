#使用莱布尼茨公式计算pi
#公式内容为：pi = 4*（1-1/3+1/5-1/7+...）
import math
p = 0
n = 0
for i in range(1,1000000,2):
     p = p +math.pow(-1,n)/i
     n += 1
print(4*p)