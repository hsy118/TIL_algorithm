def pre_rder(idx):
    if idx <= N and tree[idx][0]:
        if not tree[idx][1] and not tree[idx][2]:
            return int(tree[idx][0])
        else:
            sachik = tree[idx][0]

            if sachik == '+':
                return pre_rder(int(tree[idx][1])) + pre_rder(int(tree[idx][2]))
            elif sachik == '*':
                return pre_rder(int(tree[idx][1])) * pre_rder(int(tree[idx][2]))
            elif sachik == '-':
                return pre_rder(int(tree[idx][1])) - pre_rder(int(tree[idx][2]))
            else:
                return pre_rder(int(tree[idx][1])) / pre_rder(int(tree[idx][2]))

    return 0


T = 10

for tc in range(1, T + 1):
    N = int(input())
    tree = [['', None, None] for _ in range(N + 2)]
    for i in range(1, N + 1):
        line = input().split()
        tree[i][0] = line[1]
        for j in range(2, len(line)):
            tree[i][j - 1] = line[j]

    print(f'#{tc} {int(pre_rder(1))}')