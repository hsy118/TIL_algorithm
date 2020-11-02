T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    result = []

    # 90도
    arr90= []
    for j in range(N):
        temp = []
        for i in range(N-1, -1, -1):
            temp.append(arr[i][j])
        arr90.append(temp)

    # 180도
    arr180 = []
    for j in range(N):
        temp = []
        for i in range(N-1, -1, -1):
            temp.append(arr90[i][j])
        arr180.append(temp)

    # 270도
    arr270 = []
    for j in range(N):
        temp = []
        for i in range(N - 1, -1, -1):
            temp.append(arr180[i][j])
        arr270.append(temp)
    # 입력
    print(f"#{tc}")
    for i in range(N):
        print(''.join(list(map(str, arr90[i]))), ''.join(list(map(str, arr180[i]))), ''.join(list(map(str, arr270[i]))))

