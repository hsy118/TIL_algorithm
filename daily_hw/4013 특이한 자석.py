T = int(input())
for tc in range(1, T+1):
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        ind_i, ind_j = map(int, input().split())
        ind_i -= 1
        move = [(ind_i, ind_j)]

        temp = ind_j
        for i in range(ind_i-1, -1, -1):
            if arr[i][2] != arr[i+1][6]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        temp = ind_j
        for i in range(ind_i+1, 4):
            if arr[i][6] != arr[i-1][2]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        for ind, rot in move:
            if rot == 1:
                arr[ind] = [arr[ind].pop()] + arr[ind]
            elif rot == -1:
                arr[ind].append(arr[ind].pop(0))

    result = 0
    for i in range(4):
        result += arr[i][0] * 2 ** i
    print(f"#{tc} {result}")
