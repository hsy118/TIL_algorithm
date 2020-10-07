def heappush(v):
    global cnt
    cnt += 1
    tree[cnt] = v
    cur = cnt
    parent = cur // 2
    while parent and tree[parent] > tree[cur]:
        tree[parent], tree[cur] = tree[cur], tree[parent]
        cur = parent
        parent = cur // 2

def plus(n):
    global sum1
    n = n //2
    if n > 0:
        sum1 += tree[n]
        plus(n)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    temp = list(map(int, input().split()))
    cnt = 0
    sum1 = 0
    for i in range(N):
        heappush(temp[i])
    plus(N)
    print(f"#{tc} {sum1}")