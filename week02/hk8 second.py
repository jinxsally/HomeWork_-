#数值积分求解pi值
f = lambda x:(1-x**2)**0.5#得到圆的函数
a = -1
b = 1#设置函数的范围
from scipy.integrate import quad
val,err=quad(f,a,b)#进行定积分求解，得到pi/2值
print(val*2)