A=[25, 74, 67, 4, 69, 30, 68, 95, 39, 41]

for i in range(len(A)):
    for j in range(i):
        if A[i]<A[j]:
            A[i],A[j]=A[j],A[i]
        if A[j+1]<A[j]:
            t=A[j+1]
            A[j+1]=A[j]
            A[j]=t
print(A)