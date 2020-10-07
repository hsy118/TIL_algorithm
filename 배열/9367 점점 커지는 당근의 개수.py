for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = 0
    cnt = 1
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            if maxV < cnt:
                maxV = cnt
                cnt = 1
        elif arr[i] < arr[i+1]:
            cnt += 1
    if maxV < cnt:
        maxV = cnt

    print(f"#{tc} {maxV}")
