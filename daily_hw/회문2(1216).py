def pal(text_list, M):
    N = 100
    result=[]
    for r in range(N):
        for c in range(N-M+1):
            if text_list[r][c: c+M] == text_list[r][c: c+M][::-1]:
                result.append(text_list[r][c:c+M])
                return result[0]

    for r in range(N - M + 1):
        for c in range(N):
            col_list = []
            for i in range(M):
                col_list.append(text_list[r + i][c])
            if col_list == col_list[::-1]:
                result.append(''.join(col_list))
                return result[0]
    if len(result) == 0:
        return -1
# N =100
for tc in range(1, 11):
    t = int(input())
    arr = [input() for _ in range(100)]
    big_len = 0
    for M in range(100, 0, -1):
        char = pal(arr, M)
        if char == -1:
            continue
        else:
            big_len = len(char)
            break

    print(f'#{tc} {big_len}')
