
import math
x1 =1
x2 =3
x =(x1+x2)/2
while abs(x-math.sqrt(2))> math.exp(-10):
    x = (x1+x2)/2
    if x*x>2 :
        x2 = x
    elif x*x<2 :
        x1 = x
print(x)
import math
#笨办法 g'=g'+h
c = 2#求根号2
g = 1#初始取g'=1，（g'）^2 = 1<2,（g'+1）^2= 4>2 符合条件
p = 0.0001#精度确定为0.0001
h = 0.00001#步长
n = 0#计算增加次数
while abs(math.pow(g,2)-c)>p :
    g = g + h
    n = n + 1
print(g)
print(n)
#二分法
x1 =1
x2 =3
x =(x1+x2)/2
while abs(x*x-c)> math.exp(-20):
    x = (x1+x2)/2
    if x*x>2 :
        x2 = x
    elif x*x<2 :
        x1 = x
print(x)

print(math.sqrt(c))
