# def f(n, k):     # n열을 선택하는 행번호, k 전체 행과 열의 크기
#     if n == k:   # 모든 행에서 선택이 끝나면
#         sum = 0
#         global minV
#         for i in range(0, k):
#             sum += A[i][p[i]]
#         if minV > sum:
#             minV = sum
#     else:          # 남은 행이 있으면
#         for j in range(0, k-1):
#             if u[j] == 0:        # j가 아직 선택하지 않은 열이면
#                 u[j] = 1         # j를 표시해서 n+1 이후의 행에서 사용을 막음
#                 p[n] = j         # n번 행에서 j열을 선택했음을 기록
#                 f(n+1, k)        # 다음 행에서 열을 선택하러 이동
#                 u[j] = 0         # 다른 행에서 사용할 수 있또록 풀어줌
#
#
# T= int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     A = [list(map(int, input().split())) for _ in range(N)]
#     #사용한 컬럼을 표시할 배열
#     u = [0] * N
#     # 선택한 열을 저장 p[n]: n번 행에서 선택한 열 번호
#     p = [0] * N
#     minV = 1000000000
#     f(0, N)
#     print(f'#{tc} {minV}')

#+=======================================================================================

def f1(n, k, s):      # 열을 선택하는 행번호 n, k 전체행과 열의 크기, s n-1행까지 선택한 원소값의 합
    if n == k:        # 모든 행에서 열을 선택하면
        global minV

        if minV > s:
            minV = s
    else:        # 남은 행이 있으면
        # 사용하지 않은 열을 찾아서
        for j in range(k):
            if u[j] == 0:   # j열을 선택한적이 없으면
                u[j] = 1   # u[j]를 선택했음으로 표시
                f1(n+1, k, s +A[n][j])  # n번행까지 선택한 원소의 합을 수해서 n+1행으로 이동
                u[j] = 0
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    #사용한 컬럼을 표시할 배열
    u = [0] * N
    # 선택한 열을 저장 p[n]: n번 행에서 선택한 열 번호
    p = [0] * N
    minV = 1000000000
    # f(0, N)
    f1(0, N, 0)


    print(f'#{tc} {minV}')