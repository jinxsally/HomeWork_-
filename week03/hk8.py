
import random
import math
import time
import matplotlib.pyplot as plt
a = []#存储每个数组的长度
for i in range(1,6,1):
    a.append(int(math.pow(10,i)))
l = len(a)#判断有几个数组
r1 = [random.randint(0,1000) for _ in range(0,a[0])]
r2 = [random.randint(0,1000) for _ in range(0,a[1])]
r3 = [random.randint(0,1000) for _ in range(0,a[2])]
r4 = [random.randint(0,1000) for _ in range(0,a[3])]
r5 = [random.randint(0,1000) for _ in range(0,a[4])]
#共五个数组，每个数组长度为10的递增指数函数

def select_sort(r=[]):#选择排序
    l = len(r)
    for i in range(l):
        t = r[i]
        s = i
        for j in range(i+1,l):
            if t>r[j]:
                t = r[j]
                s = j
        r[i],r[s]=r[s],r[i]
    return

Time=[]



start = time.perf_counter()
select_sort(r1)
end = time.perf_counter()
x1 = end - start
Time.append(x1)


start = time.perf_counter()
select_sort(r2)
end = time.perf_counter()
x2 = end - start
Time.append(x2)


start = time.perf_counter()
select_sort(r3)
end = time.perf_counter()
x3 = end - start
Time.append(x3)
#
start = time.perf_counter()
select_sort(r4)
end = time.perf_counter()
x4 = end - start
Time.append(x4)
#
start = time.time()
select_sort(r5)
end = time.time()
x5 = end - start
Time.append(x5)
# 10^5通过选择排序，执行程序太慢

print(Time)

plt.semilogy(range(1,6),Time,marker='o',color='b')
plt.legend()
plt.show()

#根据分析，选择排序时间复杂度为o(n^2)，通过图像可以发现增长速度比较快，且运行时间与数据特征有较大关系。












