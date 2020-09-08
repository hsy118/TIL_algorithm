def bfs(start_i, start_j):
    #방문
    Q = []
    Q.append((start_i, start_j))
    visited[start_i][start_j] = 1
    # 반복
    while Q:
        temp = Q.pop(0)
        for di, dj in dir:
            ni = temp[0] + di
            nj = temp[1] + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                if arr[ni][nj] == 3:
                    visited[ni][nj] = visited[temp[0]][temp[1]] + 1
                    return visited[ni][nj] - 2
                else:
                    Q.append( (ni, nj) ) # 처리 예정목록에 추가
                    visited[ni][nj] = visited[temp[0]][temp[1]] + 1
    return 0 # 도착 못할 때


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dir = [(0,1), (1,0), (0, -1), (-1, 0)]
    base_i, base_j = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                base_i = i
                base_j = j
    route = bfs(base_i, base_j)
    if route == 0:
        print(f"#{tc} 0")
    else:
        print(f'#{tc} {route}')
#============================================================================
#dfs 로 해보기
def dfs(i, j, N, c):     # 가능한 모든 경로를 탐색... i, j칸에 오기까지 거쳐온 edge 갯수 c
    global minV
    if maze[i][j] == '3':
        if minV > c:
            minV = c
    else:
        v[i][j] = 1 # i,j 이후에 중복 방문 방지...
        # i, j에 대해 네 방향 좌표 생성
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                dfs(ni, nj, N, c+1)  # c 주의.
        v[i][j] = 0 # i, j 이전에 다른 경로로 부터 재 진입 허용

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]

    dir = [(0,1), (1,0), (0, -1), (-1, 0)]
    base_i, base_j = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                base_i = i
                base_j = j
    minV = 1000000
    dfs(base_i, base_j, N, 0)
    print(f'{tc} {minV}')