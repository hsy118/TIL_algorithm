di = [0, 0, -1, 1]
dj = [-1, 1,0, 0]
def bfs(v):
    q = [v]
    block[v[0]][v[1]] = 0
    level = 0
    result = 0
    while q:
        level += 1
        for _ in range(len(1)):
            v = q.pop(0)
            for a in range(4):
                if block[v[0]+di[a]][v[1]+dj[a]]:
                    if block[v[0]+di[a]][v[1]+dj[a]] == 2:
                        result += level
                        block[v[0]+di[a]][v[1]+dj[a]] = 0
                        q.append([v[0]+di[a], v[1]+dj[a]])
    return result

w, h = map(int, input().split())
block = [[0]*(w+3)]+ [[0]+[1]*(w+1)+[0]] + [[0]+[1]+[0]*(w-1)+[1]+[0] for _ in range(h-1)] + [[0]+[1]*(w+1)+[0]] +[[0]*(w+3)]
N = int(input())
for i in range(N):
    data = list(map(int, input().split()))
    if data[0] == 1:
        block[h+1][1+data[1]] = 2
    elif data[0] == 2:
        block[1][1+data[1]] = 2
    elif data[0] == 3:
        block[1][1 + data[1]] = 2
    elif data[0] == 3:
        block[h+1-data[1]][w+1] = 2
start = list(map(int, input().spli8t()))
if start[0] == 1:
    start = [h+1, 1+start[1]]
elif start[0] == 2:
    start = [1, 1+start[1]]
elif start[0] == 3:
    start = [h+1 - start[1], 1]
elif start[0] == 4:
    start = [h+1-start[1], w+1]
print(bfs(start))