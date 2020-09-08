def finder(s, g, arr):
    visited = [0] * (V + 1)
    stack = [s]
    visited[s] = 1
    while stack:
        n = stack.pop()
        if n == g:
            return 1
        for i in range(1,V+1):
            if arr[n][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stack.append(i)
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    path = [[0] * (V+1) for _ in range(V+1)]
    for e in range(E):
        n1, n2 = map(int, input().split())
        path[n1][n2] = 1
    S, G = map(int, input().split())
    ans = finder(S, G, path)
    print(f'#{tc} {ans}')