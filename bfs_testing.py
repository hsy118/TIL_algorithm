def bfs(v):
    visit[v] = 1
    que = []
    que.append(v)
    while que:
        temp = que.pop(0)
        for w in range(E):
            if arr[w][0] == temp and visit[arr[w][1]] == 0:
                val = arr[w][1]
                que.append(val)
                distance[val] = distance[temp] + 1
                visit[val] = 1




for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    visit = [0] *(V+1)

    S, G = map(int, input().split())
    distance = [0] * (V+1)
    bfs(S)

    print(distance[G])