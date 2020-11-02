def DFS(n, s):
    global result
    if n == N and s > result:
        result = s
        return
    if s <= result:
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                DFS(n + 1, s * MAP[i][n] / 100)
                visited[i] = 0

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    visited = [False] * N
    DFS(0, 1)
    print('#{} {:.6f}'.format(test_case, result * 100))