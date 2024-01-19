import numpy as np
a =eval(input())
def f(x):
    y = x**3 - a
    return y
def g(x):
    y = 3*x**2
    return y
x0 = 1
e = 10**(-9)
L =0
while abs((f(x0)-0))>e:#残差判断
    x1 = x0-f(x0)/g(x0)
    x0 =x1
    L =L+1#统计次数
print(x1)