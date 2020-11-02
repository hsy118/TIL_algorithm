def bfs(N, M):
    q = []
    q.append((0,0))
    v = [[0]*M for _ in range(N)]
    v[0][0] = 1
    while q:
        i, j = q.pop(0)
        if i == N-1 and j == M -1:
            return v[i][j]
        for di, dj in ([(0, 1), (1, 0), (0, -1), (-1, 0)]):
            ni, nj = i + di, j + dj
            if 0 <=ni < N and 0 <= nj < M:
                if maze[ni][nj] == '1' and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[i][j] + 1

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

print(bfs(N, M))