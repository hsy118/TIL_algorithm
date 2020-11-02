# 공기인 칸을 탐색
def f1(N, M):
    s = [] # 생성
    s.append((0, 0))
    v = [[0]*M for _ in range(N)] # 공기인 칸
    v[0][0] = 1
    cnt = 0
    while s: #큐가 비어있지 않으면
        i, j = s.pop()
        for k in range(4): # 공기가 잇는 칸의 상화좌우칸
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni < N and 0 <=nj < M:
                if arr[ni][nj] == 0 and v[ni][nj] == 0: # 칸의 인접, 공기, 체크 안된 공기 칸
                    s.append((ni,nj))
                    v[ni][nj] = 1
                elif arr[ni][nj] == 1: # 공기 칸 i, j 옆에 치즈인 경우..
                    arr[ni][nj] = 0 # 치즈 녹음
                    cnt += 1
    return cnt # 마지막 1시간에 노긍ㄴ 치즈 칸수 == 1시간 전에 남은 칸수 이므로

    # 공기와 닿은 치즈 지우기
    # cnt = 0
    # for i in range(1, N-1):
    #     for j in range(1, M-1): #테두리를 제외하고
    #         if arr[i][j] == 1: #치즈이고 인접칸에 공기가 있으면
    #             for r, c in ([(0, 1), (1, 0), (0, -1), (-1, 0)]):
    #                 if v[i+r][j+c] == 1:
    #                     arr[i][j] = 0 # 치즈가 녹음
    #             if arr[i][j] == 1: #녹지 않은 경우
    #                 cnt += 1
    # return cnt # 녹지 않은 개수 리턴


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 공기와 치즈인 빈 공간을 dfs로 구분한다. dfs 배귀? -> 최대 100x100이므로 불가. -> 반복
# 모두 녹을 때 까지 반복
melt = 0 # 녹은 개수
pre = 0
h = 0
while True:
    melt = f1(N, M)

    if melt == 0:
        break
    h += 1
    pre = melt
print(h)
print(pre)
# cheese = 1
# h = 0
# pre = 0
# while cheese: # 모두 녹을때 까지 반복
#     pre = cheese #이전 시간의 치즈 개수 저장
#     cheese = f1(N, M) # 1시간 경과 후 남은 치즈 개수
#     h += 1

