def quickSort(A,l,r):
    if l >= r:
        return
    i = l
    j = r
    pivotkey = A[i]
    i += 1
    while i <= j:
        while i <= j and A[i] <= pivotkey:
            i += 1
        while i <= j and A[j] > pivotkey:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]  # 直接交换元素

    A[l], A[j] = A[j], A[l]  # 将基准值移到正确的位置
    quickSort(A, l, j-1)  # 对左半部分进行排序
    quickSort(A, j+1, r)  # 对右半部分进行排序

A = [15, 90, 80, 36, 31, 54, 57, 33, 21, 99]
quickSort(A, 0, len(A) - 1)
print(A)
