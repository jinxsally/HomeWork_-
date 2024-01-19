a = input()
l =len(a)
M = []
for i in range(0,l):
    if a[i]!=' ':
        M.append(a[i])
StrM = "".join(M)
print(StrM)
