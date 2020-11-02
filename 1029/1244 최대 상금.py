def money(arr):
    sum1 = 0
    arr.reverse()
    for i in range(len(arr)):
        sum1 += int(arr[i])*(10**i)
    arr.reverse()
    return sum1

def price(i, s, N):
    if i == N:
        result.append(s)
        return
    else:
        for j in range(i, len(card)):
            card[j], card[(i % len(card))] = card[(i % len(card))], card[j]
            price(i + 1, money(card), N)
            card[j], card[(i % len(card))] = card[(i % len(card))], card[j]

T = int(input())
for tc in range(1, T+1):
    num, N = map(str, input().split())
    N = int(N)
    card = list(num)
    result = [0]
    price(0, 0, N)
    ans = max(result)
    print("#{} {}".format(tc, ans))

