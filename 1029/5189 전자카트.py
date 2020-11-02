def serial(s):
    global result
    if len(nums) == N - 1:
        # 1-2-3 합
        for i, j in nums:
            result += arr[i][j]
        # 3-1로 오는 합
        result += arr[s][0]

        real_result.append(result)
        result = 0
        return
    else:
        for k in range(1, N):
            # 비짓이 0 이면?
            if not visit[k]:
                nums.append( (s, k) )
                visit[k] = 1
                serial(k)
                # 원복
                nums.remove((s, k))
                visit[k] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    nums = []
    result = 0
    real_result = []
    # 가능한 N개의 수 // 합이 최소 값
    serial(0)
    print("#{} {}".format(tc, min(real_result)))
