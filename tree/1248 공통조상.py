def order(n):
    if n:
        if n == test1 or n == test2:
            return n
        else:
            left1, right1 = order(left[n]), order(right[n])
            if left1 + right1 == (test1 + test2):
                return n
            else:
                return left1 + right1
    else:
        return 0

def counting(n):
    global cnt
    if n:
        counting(left[n])
        counting(right[n])
        cnt += 1

N = int(input())
for tc in range(1, 11):
    V, E, test1, test2 = map(int, input().split())
    temp = list(map(int, input().split()))
    left = [0] * (V+1)
    right = [0] * (V+1)
    parent = [0] * (2 * V + 1)
    cnt = 0
    for i in range(E):
        n1 = temp[2*i]
        n2 = temp[2*i+1]
        parent[n2] = n1
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2
    deep = order(1)
    counting(deep)
    print(f"#{tc} {deep} {cnt}")
