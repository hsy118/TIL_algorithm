for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        maxI = 0
        minI = 0
        for j in range(1, 100):
            if arr[maxI] < arr[j]:
                maxI = j
            if arr[minI] > arr[j]:
                minI = j
        arr[maxI] -= 1
        arr[minI] += 1

    maxV = 0
    minV = 987654321
    for i in range(100):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]
    print(f"#{tc} {maxV-minV}")
