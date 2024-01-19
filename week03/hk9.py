<<<<<<< HEAD
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

def merge(p,q,m,r):
    i = p
    j = m+1
    c = []
    while i<=m and j <=q:
        if r[i]<r[j] :
            c.append(r[i])
            i+=1
        else:
            c.append(r[j])
            j += 1
    while i<=m:
        c.append(r[i])
        i += 1
    while j<=q:
        c.append(r[j])
        j += 1
    r[p:q+1] = c


def merge_sort(p,q,r=[]):
    if p == q:
        return
    m = (p+q)//2
    merge_sort(p,m,r)
    merge_sort(m+1,q,r)
    merge(p,q,m,r)

Time = []

start = time.perf_counter()
merge_sort(0,len(r1)-1,r1)
end = time.perf_counter()
x1 = end -start
Time.append(x1)


start = time.perf_counter()
merge_sort(0,len(r2)-1,r2)
end = time.perf_counter()
x2 = end -start
Time.append(x2)


start = time.perf_counter()
merge_sort(0,len(r3)-1,r3)
end = time.perf_counter()
x3 = end -start
Time.append(x3)

start = time.perf_counter()
merge_sort(0,len(r4)-1,r4)
end = time.perf_counter()
x4 = end -start
Time.append(x4)

start = time.perf_counter()
merge_sort(0,len(r5)-1,r5)
end = time.perf_counter()
x5 = end -start
Time.append(x5)

plt.semilogy(range(1,6),Time)
plt.legend
plt.show()

#根据分析，归并排序时间复杂度为o(nlgn)，由图像可知，在对数坐标图像下大致呈线性变化。且在数据量为10^5下，运行时间明显比选择排序加快。





=======
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

def merge(p,q,m,r):
    i = p
    j = m+1
    c = []
    while i<=m and j <=q:
        if r[i]<r[j] :
            c.append(r[i])
            i+=1
        else:
            c.append(r[j])
            j += 1
    while i<=m:
        c.append(r[i])
        i += 1
    while j<=q:
        c.append(r[j])
        j += 1
    r[p:q+1] = c


def merge_sort(p,q,r=[]):
    if p == q:
        return
    m = (p+q)//2
    merge_sort(p,m,r)
    merge_sort(m+1,q,r)
    merge(p,q,m,r)

Time = []

start = time.perf_counter()
merge_sort(0,len(r1)-1,r1)
end = time.perf_counter()
x1 = end -start
Time.append(x1)


start = time.perf_counter()
merge_sort(0,len(r2)-1,r2)
end = time.perf_counter()
x2 = end -start
Time.append(x2)


start = time.perf_counter()
merge_sort(0,len(r3)-1,r3)
end = time.perf_counter()
x3 = end -start
Time.append(x3)

start = time.perf_counter()
merge_sort(0,len(r4)-1,r4)
end = time.perf_counter()
x4 = end -start
Time.append(x4)

start = time.perf_counter()
merge_sort(0,len(r5)-1,r5)
end = time.perf_counter()
x5 = end -start
Time.append(x5)

plt.semilogy(range(1,6),Time)
plt.legend
plt.show()

#根据分析，归并排序时间复杂度为o(nlgn)，由图像可知，在对数坐标图像下大致呈线性变化。且在数据量为10^5下，运行时间明显比选择排序加快。





>>>>>>> 9e496b9d40cd0a26c8f8b94ba1113995f15e8ac2
