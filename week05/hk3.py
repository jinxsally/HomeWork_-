#插入排序算法
def insert_sort(a=[]):
    l = len(a)
    for i in range(1,l):
        j = i-1#前一个数
        t = a[i]#将比较的数值提取出来
        while j>=0:
            if a[j]>t:#如果前面有比t值大的
                a[j+1]=a[j]#将该值移后一位
                j-=1#前进一位
            else:
                break
        a[j+1]=t#本来该j+1的位置为空，应该填入t值
    return

arr = input().split()#输入数组
insert_sort(arr)
for i in range(len(arr)):#将字符串数组转换为整数数组
    arr[i]=int(arr[i])
print(arr)
