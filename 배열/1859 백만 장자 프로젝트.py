"""
미래에 비싼 값이 있으면 이익
미래에 비싼 값 없으면 안삼
미래 값 기준 으로 이익 빼기
기준 0
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    profit = 0
    maxV = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if maxV > arr[i]:
            profit += maxV - arr[i]
        elif maxV <= arr[i]:
            maxV = arr[i]

    print(f"#{tc} {profit}")







