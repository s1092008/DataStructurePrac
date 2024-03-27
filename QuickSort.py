A=[15, 90, 80, 36, 31, 54, 57, 33, 21, 99]


r=len(A)-1

def quickSort(A,l,r):
    print(A)
    if l>=r:
        return
    i=l
    j=r
    pivotkey=A[i]
    i+=1
    while i<=j:
        while A[i]<=pivotkey:
            i+=1
        while A[j]>pivotkey:
            j-=1
        if i<=j:   
            A[i], A[j] = A[j], A[i]
    A[l],A[j]=A[j],A[l]
    quickSort(A,l,j-1)
    quickSort(A,j+1,r)
    
    
quickSort(A,0,r)
print(A)