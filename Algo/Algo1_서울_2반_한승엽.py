def solve(N, C, X, Y, K, R):
    global sum1
    if 0 <= (X + K - 1) <= N and 0 <= (Y + K - 1) <= N:
        angle = (C % 360)
        if angle == 90:
            #회전 시키기
            for c in range(X-1, X+K-1):
                temp = []
                for r in range(Y+K-2, Y-2, -1):
                    temp.append(original_arr[r][c])
                rot.append(temp)
            # 출력 행 찾기
            if Y <= R < Y+K:
                # 출력할 row
                row = abs(Y-R)
                sum1 = sum(rot[row])
                for j in range(N):
                    # (R-1)줄에서 바껴진 줄이 아니면 더한다,
                    if not (X-1 <= j < X+K-1):
                        sum1 += original_arr[R-1][j]
            else:
                for j in range(N):
                    sum1 += original_arr[R-1][j]

        elif angle == 180:
            # 회전 시키기
            for r in range(Y+K-2, Y-2, -1):
                temp = []
                for c in range(X+K-2, X-2, -1):
                    temp.append(original_arr[r][c])
                rot.append(temp)
            # 출력 행 찾기
            if Y <= R < Y + K:
                # 출력할 row
                row = abs(Y - R)
                sum1 = sum(rot[row])
                for j in range(N):
                    # (R-1)줄에서 바껴진 줄이 아니면 더한다,
                    if not (X - 1 <= j < X + K - 1):
                        sum1 += original_arr[R - 1][j]
            else:
                for j in range(N):
                    sum1 += original_arr[R - 1][j]

        elif angle == 270:
            # 회전 시키기
            for c in range(X+K-2, X-2, -1):
                temp = []
                for r in range(Y-1, Y+K-1):
                    temp.append(original_arr[r][c])
                rot.append(temp)
            # 출력 행 찾기
            if Y <= R < Y + K:
                # 출력할 row
                row = abs(Y - R)
                sum1 = sum(rot[row])
                for j in range(N):
                    # (R-1)줄에서 바껴진 줄이 아니면 더한다,
                    if not (X - 1 <= j < X + K - 1):
                        sum1 += original_arr[R - 1][j]
            else:
                for j in range(N):
                    sum1 += original_arr[R - 1][j]

        elif angle == 0:
            for j in range(N):
                sum1 += original_arr[R-1][j]
        return sum1
    else:
        sum1 = -1
        return sum1

T = int(input())
for tc in range(1, T+1):
    # N 배열 크기, C - 회전각도, X / Y 시작 위치, K 부분영역 가로세로 값, R- 출력 행
    N, C, X, Y, K, R = map(int, input().split())
    original_arr = [list(map(int, input().split())) for _ in range(N)]
    sum1 = 0
    rot = []
    solve(N, C, X, Y, K, R)

    print(f"#{tc} {sum1}")
