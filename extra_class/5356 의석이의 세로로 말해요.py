T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    # 가장 긴 줄 찾기
    max_long = 0
    for i in arr:
        if len(i) > max_long:
            max_long = len(i)
    # 배열 길이 맞추기
    for i in range(5):
        if len(arr[i]) <= max_long:
            arr[i] += [0] * (max_long - len(arr[i]))

    answer = ""
    for i in range(max_long):
        for j in range(5):
            if arr[j][i] == 0:
                continue
            else:
                answer += arr[j][i]

    print(f'#{tc} {answer}')