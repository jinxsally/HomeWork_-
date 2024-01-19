#求解f(x)=x^3-c=0的解
#f'(x)=3*x^2
#则迭代表达式为：x = -y/3*x^2 +x
import math
def f(x,c):
    while abs(math.pow(x,3)-c)>math.exp(-20):
        y = math.pow(x,3) - c
        x = -y/(3*x*x) + x
    return x
c = 10#假设c为10
x = c/2
x = f(x,c)
print(x)
print(x*x*x)#验证结果的正确性