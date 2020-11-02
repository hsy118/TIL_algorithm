def solve(list1):
    result = ""
    for i in list1:
        if i > 1:
            result = "No"
            break
        else:
            result = "Yes"
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_l = [0] * 8
    for i in range(N):
        new_l[arr[i]] += 1
    result = solve(new_l)

    print(f"#{tc} {result}")