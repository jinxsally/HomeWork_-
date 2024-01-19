a = input()
l = len(a)
m=0
for i in range(1,l-1):
    for j in range(i,l-1):
        if a[i]==a[j] and m==0:
            print('Yes')
            m=1
if m==0 :
   print('No')