def post(n):
    global cnt
    if n == 0:
        return 0
    else:
        return 1 + post(tree[n][0]) + post(tree[n][1])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1
    temp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]
    for i in range(E):
        n1, n2 = temp[i*2], temp[i*2+1]
        if tree[n1][0] == 0:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1

    for i in range(1, len(tree)):
        if tree[i][2] == 0:
            root = i
    cnt = 0
    result = post(N)
    print(f"#{tc} {result}")