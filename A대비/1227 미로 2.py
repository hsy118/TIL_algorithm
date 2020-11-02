def bfs(s):
    visit = [[0] * 100 for _ in range(100)]
    visit[s[0]][s[1]] = 1
    que = []
    que.append(s)
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while que:
        temp = que.pop(0)
        if maze[temp[0]][temp[1]] == 3:
            return visit[temp[0]][temp[1]]
        for di, dj in dir:
            ni = temp[0] + di
            nj = temp[1] + dj
            if maze[ni][nj] != 1 and 0 <= ni < 100 and 0 <= nj < 100 and visit[ni][nj] == 0:
                    visit[ni][nj] = visit[temp[0]][temp[1]]+1
                    que.append( (ni, nj) )
    return 0


def dfs(s):
    stack = []
    stack.append(s)
    # visit = [[0]*100 for _ in range(100)] 이렇게 할 수도 있는데 지나가면 벽(1)으로 바꿀꺼임
    maze[s[0]][s[1]] = 1
    while stack:
        i, j = stack.pop()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if maze[ni][nj] == 3:
                return 1
            elif maze[ni][nj] == 0:
                stack.append((ni, nj))
                maze[ni][nj] = 1
    return 0


def dfs2(s):
    stack = []
    stack.append(s)
 
    while stack:
        i, j = stack.pop()
        if maze[i][j] != 1:
            maze[i][j] = 1

            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if maze[ni][nj] == 3:
                    return 1
                elif maze[ni][nj] == 0:
                    stack.append((ni, nj))

    return 0

for tc in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start = (i, j)
                break

    # ans = bfs(start)
    ans = dfs2(start)
    print("#{} {}".format(N, ans))
