def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    else:
        return paper(n-1) + (2*paper(n-2))


T= int(input())
for tc in range(1, T+1):
    N = (int(input()) // 10)
    put_paper = paper(N)
    print(f'{tc} {put_paper}')