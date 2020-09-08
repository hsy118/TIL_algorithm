direc = [(-1,0), (0,1),(1,0),(0,-1)] #상우하좌
# 전부 검색
def find(i, j):
    global cnt
    # visit = [[0] * (N) for _ in range(N)]
    Q = []
    Q.append((i,j))
    while Q:
        temp = Q.pop(0)
        for di, dj in direc:
            ni = temp[0] + di
            nj = temp[1] + dj
            if 0<=ni<N and 0<=nj<N:
                if (arr[ni][nj] - arr[temp[0]][temp[1]]) == 1:
                    cnt += 1
                    Q.append((ni,nj))
                    # visit[ni][nj] = visit[temp[0]][temp[1]] + 1


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0 # 최대 칸 이동수
    cnt = 1  #칸 이동 수
    num = N**2  # 방 번호

    for i in range(N):
        for j in range(N):
            cnt = 1
            find(i,j)
            if cnt == maxV:  # 칸 이동 수랑 최고 이동 수랑 같아도
                if arr[i][j] < num:    # 방번호 작은걸 또 업데이트
                    maxV, num = cnt, arr[i][j]
            elif cnt > maxV:      #최고 칸 이동수를 찾으면
                maxV, num = cnt, arr[i][j]     # 방번호, 최고칸 업데이트

    print(f"#{tc} {num} {maxV}")
