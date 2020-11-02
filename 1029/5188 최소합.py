def f(i,j,s,N):
    global minV, cnt
    cnt += 1
    if i == N-1 and j == N-1:
        if minV> s+arr[i][j]:
            minV = s+arr[i][j]
    elif s >= minV:
        return
    else:
        if i+1 < N:
            f(i+1, j, s+arr[i][j], N)
        if j+1 < N:
            f(i, j+1, s+arr[i][j], N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 987654321
    cnt = 0

    f(0, 0, 0, N)
    print("#{} {}".format(tc, minV))