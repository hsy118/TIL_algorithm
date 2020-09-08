def f(v):
    visit[v] = 1
    for j in arr[v]:
        if not visit[j]:
            f(j)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # N: 사람의 수 M : 알고있는 관계의 수
    arr = [[] * (N+1) for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        # 관계만 넣기
        arr[a].append(b)
        arr[b].append(a)
    visit = [0] * (N + 1)
    cnt = 0
    for i in range(1, N+1):
        if visit[i]:
            continue
        f(i)
        cnt += 1
    print(f'#{tc} {cnt}')
#==============
#bfs
