for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    sum1 = 0 # 열
    for i in range(100):
        if sum1 < sum(arr[i]):
            sum1 = sum(arr[i])
    maxV = sum1  # 열의 최댓값이 맥스밸류

    sum2 = 0
    for i in range(100):
        sum2 = 0
        for j in range(100):
            sum2 += arr[j][i]
        if sum2 > maxV:
            maxV = sum2

    sum3 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum3 += arr[i][j]
    sum4 = 0
    for i in range(100):
        for j in range(100):
            if i + j == 99:
                sum4 += arr[i][j]
    if maxV <sum3:
        maxV = sum3
    if maxV < sum4:
        maxV = sum4
    print(f"#{tc} {maxV}")