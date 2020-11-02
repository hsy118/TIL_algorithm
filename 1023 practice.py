"""
0000000111100000011000000111100110000110000111100111100111111001100111
"""
T = int(input())
for tc in range(1, T+1):

    case = list(map(int, input()))
# 반복문
# 7개씩 반복문
# 7개 돌고 앞에 7개 지운다
# 리스트 길이 0 되면 끝
    result = []
    temp = []
    temp_sum = 0
    while case:
        temp = []
        for i in range(7):
            temp.append(case[i])
        temp = temp[::-1]

        for i in range(7):
            if temp[i] == 1:
                temp_sum += (2 ** i)
        result.append(temp_sum)
        temp_sum = 0
        del case[:7]

    ans = ''
    for i in range(len(result)):
        string = str(result[i])
        ans += f"{string} "
    print(f"#{tc} {ans}")

##
# result = []
# temp = []
# temp_sum = 0
# for i in range(7):
#     temp.append(case[i])
# temp.reverse()
# print(temp)
# for i in range(len(temp)):
#     if temp[i] == 1:
#         temp_sum += (2 ** i)
# result.append(temp_sum)
# temp_sum = 0

