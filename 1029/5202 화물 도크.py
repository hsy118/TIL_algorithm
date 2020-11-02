T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))
    # 순서 대로
    for i in range(N):
        for j in range(i, N):
            if arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]
    # 순서대로 시간별로 가능한 항목들 넣기
    result = []
    visit = [0] * N
    result.append(arr[0])
    visit[0] = 1
    while True:
        # elimination
        for i in range(N):
            # 비교 // result에 있는 값이랑 // 끝나는 시간 안에 시작 시간이 포함되어 있으면 확인하고 다음 꺼 보기
            if result[-1][-1] > arr[i][0]:
                visit[i] = 1
        if 0 not in visit:
            break
        ind = 0
        minV = 987654321
        for i in range(N):
            # 포함되지 않고, 다음 시작시간이 끝나느 시간보다 크면 추가
            if visit[i] == 0 and result[-1][-1] <= arr[i][0] and arr[i][1] < minV:
                ind = i
                minV = arr[i][0]
        #추가
        result.append(arr[ind])
        ans = len(result)
    print("#{} {}".format(tc, ans))

# a = (0, 1)
# print(a[-1])
# print(a[1])
