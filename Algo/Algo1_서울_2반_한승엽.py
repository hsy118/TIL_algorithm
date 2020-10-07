T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N-행의 개수 M-열의 갯수, K-테두리 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 변수 초기화
    result = []
    #가로는 N-K만큼, 세로는 M-K만큼 순회
    for r in range(N - K + 1):
        for c in range(M - K + 1):
            cnt = 0
            for i in range(r+0, r+K):
                for j in range(c+0, c+K):
                    # i가 시작줄 혹은 마지막 줄 일때 합
                    if i == (r+0) or i == (r+K-1):
                        cnt += arr[i][j]
                    # j가 첫 열 줄, 마지막 열줄 일때 합
                    if j == (c+0) or j == (c+K-1):
                        cnt += arr[i][j]
            # 두번씩 더해진 각 꼭지점을 한번씩 빼준다
            cnt = cnt - (arr[r+0][c+0] + arr[r+0][c+K-1] + arr[r+K-1][c+0] + arr[r+K-1][c+K-1])
            # 합들을 리스트에 저장
            result.append(cnt)
    # 합들의 최대-최소 = ans
    ans = max(result) - min(result)
    # 출력
    print(f"#{tc} {ans}")