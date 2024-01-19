<<<<<<< HEAD
import math
c = 2


x = c/2
y = math.pow(x,2) -2#此时c为2
while abs(x-math.sqrt(2)>math.exp(-20)):
    x = -y/(2*x) + x
    y = x**2 -2
print(x)


x = c/4
y = math.pow(x,2) -2#此时c为2
while abs(x-math.sqrt(2)>math.exp(-20)):
    x = -y/(2*x) + x
    y = x**2 -2
print(x)


x = c
y = math.pow(x,2) -2#此时c为2
while abs(x-math.sqrt(2)>math.exp(-20)):
    x = -y/(2*x) + x
    y = x**2 -2
print(x)
print(math.sqrt(2))
=======
import math
c = 2


x = c/2
y = math.pow(x,2) -2#此时c为2
while abs(x*x-c)>math.exp(-20):
    x = -y/(2*x) + x
    y = x**2 -c
print(x)


x = c/4
y = math.pow(x,2) -2#此时c为2
while abs(x*x-c)>math.exp(-20):
    x = -y/(2*x) + x
    y = x**2 -c
print(x)


x = c
y = math.pow(x,2) -2#此时c为2
while abs(x*x-c)>math.exp(-20):
    x = -y/(2*x) + x
    y = x**2 -c
print(x)

print(math.sqrt(2))
#发现改变起始值g，不会对结果有影响
>>>>>>> 9e496b9d40cd0a26c8f8b94ba1113995f15e8ac2
