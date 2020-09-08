T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        short = A
        long = B
    elif N > M:
        long = A
        short = B
    maxV = 0
    for i in range(len(long) - len(short)+ 1):
        sum = 0
        for j in range(len(short)):
            sum += short[j] * long[j+i]
        if maxV < sum:
            maxV = sum
    print(f'#{tc} {maxV}')
