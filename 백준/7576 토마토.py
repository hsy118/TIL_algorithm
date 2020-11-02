from collections import deque

def bfs(N, M):
    q = deque()
    v = [[0] *M for _ in range(N)]
    for i in range(N):
        for j in range(M): #익은 토마토 시작점
            if tomato[i][j] == 1:
                q.append((i, j)) # 시작점 인큐
                v[i][j] = 1 # 시작점 표시
    last = 0
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if tomato[ni][nj] == 0 and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[i][j] + 1
                    last = v[i][j]  # v[ni][nj] - 1 이 실제 경과 일 수, 가장 마지막이 최대가 됨
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0 and v[i][j] == 0: # 안익은 토마토,
                return -1
    return last

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

print(bfs(N, M))