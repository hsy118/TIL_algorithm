def qsort(A, l, r):
    if l<r:
        p = partition(A, l, r)
        qsort(A, l, p-1)
        qsort(A, p+1, r)

def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
            while i <= j and A[j] >= p:
                j -= 1
        if 