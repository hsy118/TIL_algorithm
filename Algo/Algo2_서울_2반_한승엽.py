def bfs(r, c):
    global cnt
    # 방문
    que = []
    que.append( (r,c) )
    visit[r][c] = 1
    while que:
        # 처리할 좌표
        temp = que.pop(0)
        # 폭발 범위
        range = arr[temp[0]][temp[1]]
        t = 1
        # 폭발 범위만큼 우,좌,상,하 로 이동
        while t <= range:
            # 방향 설정
            for di, dj in dir:
                # 폭발 범위 1, 2, ... 한칸식 늘려가면서 폭발 범위까지 탐색
                ni = temp[0] + (di*t)
                nj = temp[1] + (dj*t)
                # 유효 구간 확인
                if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
                    if arr[ni][nj] != 0:
                        # 방문 표시
                        visit[ni][nj] = 1
                        cnt += 1
                        # 다음에 탐색할 좌표 저장
                        que.append((ni, nj))
            t += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start_i, start_j = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] *(N) for _ in range(N)]
    dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 우, 좌, 상, 하
    # 폭발 갯수 카운트
    cnt = 1
    bfs(start_i, start_j)
    print(f"#{tc} {cnt}")