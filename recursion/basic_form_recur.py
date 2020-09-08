def f(n, k):
    if n==k:
        print(A)

    else:
        B[n] = A[n]
        f(n+1, k)

A = [1,2,3]
B = [0, 0, 0]
f(0,3)
#===================================
def f(n, k):
    if n==k:
        print(A)

    else:
        A[n] = n+1
        f(n+1, k)

A = [0] * 10
f(0,10)