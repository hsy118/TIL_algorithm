def sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        mid = len(list1) // 2
        right = sort(list1[mid:])
        left = sort(list1[:mid])
    return merge(left, right)

def merge(left, right):
    global cnt

    left_len = len(left)
    right_len = len(right)
    result = [0] * (left_len + right_len)
    left_point, right_point = 0, 0
    i = 0
    if left[-1] > right[-1]:
        cnt += 1
    while left_point != left_len and right_point != right_len:
        if left[left_point] <= right[right_point]:
            result[i] += left[left_point]
            i += 1
            left_point += 1
        else:
            result[i] += right[right_point]
            i += 1
            right_point += 1

    if left_point != left_len:
        while left_point != left_len:
            result[i] += left[left_point]
            i += 1
            left_point += 1
    if right_point != right_len:
        while right_point != right_len:
            result[i] += right[right_point]
            i += 1
            right_point += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = sort(arr)
    real_ans = ans[N//2]
    print("#{} {} {}".format(tc, real_ans, cnt))
