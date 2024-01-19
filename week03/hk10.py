<<<<<<< HEAD
n = eval(input())
A = []
for i in range(0,n):
    A.append(eval(input()))
B = []
for i in range(0,n):
    B.append(1)
    for j in range(0,n):
        if j !=i:
           B[i] *= A[j]

=======
n = eval(input())
A = []
for i in range(0,n):
    A.append(eval(input()))
B = []
for i in range(0,n):
    B.append(1)
    for j in range(0,n):
        if j !=i:
           B[i] *= A[j]

>>>>>>> 9e496b9d40cd0a26c8f8b94ba1113995f15e8ac2
print(B)