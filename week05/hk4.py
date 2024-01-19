def select_sort(array):
    for i in range(len(array)):
        x = i# min index
        for j in range(i,len(array)):
            if array[j]<array[x]:
                x=j
            array[i],array[x]=array[x],array[i]
    return array
#计算时间复杂度：f(n)=f(n-1)+n-1 -->f(n)=0(n^2)
#计算空间复杂度：仅使用一个数组，0(n)