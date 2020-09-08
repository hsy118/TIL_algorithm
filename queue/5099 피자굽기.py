T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 화덕의 크기  M 피자갯수
    arr = list(map(int, input().split()))
    arr = [(i+1, v) for i, v in enumerate(arr)]  #i 에다가 나주엥 +1
    # print(arr)
    que = []
    # 한바퀴 돌때마다 치즈는 C//2 가 됌
    for i in range(N):
        que.append(arr[i])

    i = N
    while True:
        p_index, pizza = que.pop(0)
        pizza = pizza // 2
        if pizza == 0:
            if i < M:
                que.append(arr[i])
                i += 1
        else:
            que.append((p_index, pizza))

        if len(que) == 1:
            break
    print(f"#{tc} {que[0][0]}")
