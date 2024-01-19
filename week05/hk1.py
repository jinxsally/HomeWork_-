import math
a=eval(input())
t=int(math.sqrt(a))+1
m=0
for i in range(2,t):
    if a%i ==0:
        print("a不是质数")
        m=1
        break
if m==0:
    print("a是质数")
