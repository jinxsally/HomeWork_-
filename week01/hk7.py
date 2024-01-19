L = eval(input())
l= len(L)
M =[]
for i in range(1,l+1):
    M.append(L[l-i])
print(M)