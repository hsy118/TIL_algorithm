T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sum = 0
    s = N // 2
    e = N // 2
    for i in range(N):
        if i == 0:
            s = N // 2
            e = N // 2
            for j in range(s, e+1):
                sum += arr[i][j]
        if 1 <= i <= (N // 2):
            s -= 1
            e += 1
            for j in range(s, e+1):
                sum += arr[i][j]
        if i > (N // 2):
            s += 1
            e -= 1
            for j in range(s, e+1):
                sum += arr[i][j]
    print(f'#{tc} {sum}')
