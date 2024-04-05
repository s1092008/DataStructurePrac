A=[4, 61, 3, 23, 74, 6, 36, 88, 40, 75]

t=A[0]
for i in range(len(A)):
    for j in range(i):
        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
print(A)