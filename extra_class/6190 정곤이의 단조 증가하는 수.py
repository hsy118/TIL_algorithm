T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =list(map(int, input().split()))
    result = -1
    for i in range(N):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            status = 10
            while num >= 1:
                n1 = num % 10
                num = num // 10
                if status < n1:
                    break
                status = n1
            else:
                num = arr[i] * arr[j]
                if result < num:
                    result = num

    print(f"#{tc} {result}")