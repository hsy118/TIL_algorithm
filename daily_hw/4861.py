T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []

    arr = [input() for _ in range(N)]
    #가로
    for r in range(N):
        for c in range(N-M+1):
            if arr[r][c: c+M] == arr[r][c: c+M][::-1]:
                result.append(arr[r][c:c+M])
    #세로
    for r in range(N - M + 1):
        for c in range(N):
            col_list = []
            for i in range(M):
                col_list.append(arr[r + i][c])
            if col_list == col_list[::-1]:
                result.append(''.join(col_list))

    print(f'#{tc} {result[0]}')

