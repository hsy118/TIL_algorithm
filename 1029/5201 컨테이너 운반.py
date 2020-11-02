# T = int(input())
# for tc in range(1, T+1):
#     containor, truck = map(int, input().split())
#     weight = list(map(int, input().split()))
#     power = list(map(int, input().split()))
#
#     visit_truck = [0] * truck
#     visit_containor = [0] * containor
#     # 트럭 다 확인 할때 까지
#     while True:
#         #힘쎈 트럭
#         maxV = 0
#         for i in range(truck):
#             if maxV < power[i] and visit_truck[i] == 0:
#                 pick, maxV = power[i], power[i]
#                 max_index = i
#
#         visit_truck[max_index] = 1
#
#         # 무거운 화물
#         heavy = 0
#         for j in range(containor):
#             if heavy < weight[j] and visit_containor[j] == 0 and pick >= weight[j]:
#                 heavy = weight[j]
#                 heavy_index = j
#         status = 1
#         # 화물 옮기면 비짓 체크
#         if pick >= heavy:
#             visit_containor[heavy_index] = 1
#         if 0 not in visit_truck:
#             status = 0
#         if 0 not in visit_containor:
#             status = 0
#         if status == 0:
#             break
#     sum1 = 0
#     for i in range(containor):
#         if visit_containor[i] == 1:
#             sum1 += weight[i]
#     print("#{} {}".format(tc, sum1))


#========================================================================
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    con_weight = list(map(int, input().split()))
    truck_weight = list(map(int, input().split()))
    visit = [0] * M
    ans = 0
    for i in range(M):
        result = 0
        for w in con_weight:
            if truck_weight[i] >= w and w >= result:
                result = w
        if result != 0:
            con_weight.remove(result)
        ans += result
    print("#{} {}".format(tc, ans))

