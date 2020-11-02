def solve(k):
    global ans
    if k == len(food):
        tsum = 0
        for h in range(len(home)):
            for f in range(len(subset)):
                if subset[f]:
                    tmin = min(tmin, dist[f][h])
            tsum += tmin
        if ans> tsum:
            ans = tsum
    else:
        pass

for tc in range(1, int(input()) + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    home, food = [], []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                home.append((i, j))
            elif mat[i][j] > 1:
                food.append((i, j, mat[i][j]))

    dist = [[0] * len(home) for i in range(len(food))]
    for i in range(len(food)):
        for j in range(len(home)):
            dist[i][j] = abs(food[i][0] - home[j][0] + abs(food[i][1] - home[j][1]))
