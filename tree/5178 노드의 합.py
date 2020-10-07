def post(n):
    if n <= N:
        post(n*2)
        post(2*n+1)
        if (2 * n + 1) <= N:
            tree[n] = tree[n*2] + tree[2* n + 1]
        elif (2 * n) <= N:
            tree[n] = tree[2*n]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N 노드 갯수 M 리프 노드 갯수  값 출력할 L
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    print(tree)
    post(1)
    ans = tree[L]
    print(f"#{tc} {ans}")