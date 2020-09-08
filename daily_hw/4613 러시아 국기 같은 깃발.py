T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N 세로 M 가로
    arr = [list(input()) for _ in range(N)]
    minV = 1000000000

    c1 = 0
    for w in range(N-2): # w가 M- (N-2) 줄이면 각각 색띠
        for j in range(M):
            if arr[w][j] != "W":
                c1 += 1
        c2 = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if arr[b][j] != "B":
                    c2 += 1
            c3 = 0
            for r in range(b+1, N):
                for j in range(M):
                    if arr[r][j] != "R":
                        c3 += 1

            count = c1 + c2 + c3
            if minV > count:
                minV = count

    print(f"#{tc} {minV}")
