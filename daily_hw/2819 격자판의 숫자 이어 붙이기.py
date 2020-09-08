def f(i, j, n):
    if n==7:
        num.append(''.join(map(str, s)))
    else:
        s[n] = arr[i][j]
        for di, dj in [(0,1), (1,0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<4 and 0<=nj<4:
                f(ni, nj, n+1)

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    num = []
    s = [0] * 7
    for i in range(4):
        for j in range(4):
            f(i, j, 0)
    print(f'{len(set(num))}')
#########################################################################
def f1(i, j, n, txt):
    if n == 7:
        num.append(txt)
    else:
        # v[i][j] = 1
        for di, dj in [(0,1), (1,0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<4 and 0<=nj<4:       # 한번 쓴거 못쓰게 할꺼면 여기에 andv[ni][nj] ==0 : 해야게찌
                f1(ni, nj, n+1, txt+str(arr[i][j]))
        # v[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    num = []
    s = [0] * 7
    for i in range(4):
        for j in range(4):
            f(i, j, 0)
    print(len(set(num))