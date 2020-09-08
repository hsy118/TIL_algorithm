def f(i, j, N): # 모든칸에 방문
    v[i][j] = 1
    # 인접(미로를 벗어나지 않고 벽이 아니면)하고 방문하지 않은 칸이면 이동
    for di, dj in [(0,1), (1,0), (0,-1),(-1,0)]:
        ni, nj = i+di, j+dj # i, j 칸의 주변 칸
        if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and v[ni][nj] == 0:
            f(ni,nj,N)

def f1(i, j, N):
    if maze[i][j] == '3':
        return 1
    else:
        v[i][j] = 1
        # 인접(미로를 벗어나지 않고 벽이 아니면)하고 방문하지 않은 칸이면 이동
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj  # i, j 칸의 주변 칸
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and v[ni][nj] == 0:
                if f1(ni, nj, N):
                    return 1
        return 0   # 가능한 4방향을 탐색해도 목적지가 없는 경우



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    v = [[0] *N for _ in range(N)]
    starti = 0
    startj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                starti, startj = i, j
    #f(starti, startj, N)
    print(f'#{tc} {f1(starti, startj, N)}')
