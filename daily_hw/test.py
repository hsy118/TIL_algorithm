# def dps(stx, goal, V):
#     stack = []
#     stack.append(stx)
#     v = [0]*(V+1)
#
#     while stack:
#         n = stack.pop()
#         if v[n] == 0:
#             v[n] = 1
#             if n == goal:
#                 return 1
#             for i in range(1, (V+1)):
#                 if adj[n][i] == 1:
#                     stack.append(i)
#     return 0
def f3(n, goal, V):
    visited[n] = 1
    if n == goal:
        return 1
    else:
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                if f3(i, goal, V):
                    return 1
        return 0



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    stx, goal = map(int, input().split())

    visited = [0]*(V+1)
    print(f'#{tc} {f3(stx, goal, V)}')
