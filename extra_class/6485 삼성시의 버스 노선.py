T = int(input())
for tc in range(1, T+1):
    N = int(input())       # 노선의 갯수
    route = []
    for _ in range(N):
        bus = [0] * 5001
        A, B = map(int, input().split())
        for s in range(len(bus)):
            if A <= s <= B:
                bus[s] = 1
        route.append(bus)

    P = int(input())
    for _ in range(P):
        int(input())

    # 정거장 별로 노선의 갯수를 표현하는 리스트
    num_station = []
    sum = 0
    for i in range(len( route[0] )):
        sum = 0
        for j in range(N):
            sum += route[j][i]
        num_station.append(sum)
    # 출력을 위한 반복문
    answer = ""
    for i in num_station:
        if i != 0:
            answer += str(i) + " "
        if i != 0 and i == len(num_station)-1 :
            answer += str(i)

    print(f'#{tc} {answer}')
    #메모리 너무 먹어서 실패...
#+=====================================
# T = int(input())
# for tc in range(1, T+1):
#     count = [0] * 5001
#     N = int(input())
#     for i in range(1, N+1):
#         a, b = map(int, input().split())
#         for j in range(a, b+1):
#             count[j] += 1
#
#     P = int(input())
#     print(f"#{tc}", end= " ")
#     for i in range(P):
#         station = int(input())
#         print(f"{count[station]}", end=" ")
#     print()
