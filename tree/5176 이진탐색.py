def inorder(n):
    global i
    if n <= N:
        inorder(n*2)
        tree[n] = i
        i += 1
        inorder(n*2+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N 으로 완전이진트리 만들고, 루트랑 N//2번 노드 값
    tree = [0] * (N + 1)

    i = 1
    inorder(1)
    # print(tree)
    idx1 = tree[1]
    half = tree[N//2]
    print(f"#{tc} {idx1} {half}")
