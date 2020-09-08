T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    word = 0
    count = 0
    #가로
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            elif arr[i][j] == 0:
                count = 0
            # 세다가 K개 되면
            if count == K and (j == (N-1) or arr[i][j+1] == 0):
                word += 1
                count = 0
            if j == N-1:
                count = 0
    #세로
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            elif arr[i][j] == 0:
                count = 0
            if count == K and (i == (N-1) or arr[i+1][j] == 0):
                word += 1
                count = 0
            if i == N-1:
                count = 0
    print(f'#{tc} {word}')
