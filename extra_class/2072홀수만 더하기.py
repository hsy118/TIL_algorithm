import sys
sys.stdin = open("2072_input.txt")
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    odd_sum = 0
    for i in range(len(arr)):
        if arr[i] % 2 ==1:
            odd_sum += arr[i]

    print(f'#{tc} {odd_sum}')
