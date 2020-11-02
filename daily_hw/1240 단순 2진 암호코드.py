"""
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
"""
# digits = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     decode = [0] * 8
#     ans = 0
#     for _ in range(N):
#         line = input()
#         ptr = 0
#         for i in range(M):
#             if line[i] == '1': ptr = i
#         if ptr >= 55:
#             line = line[ptr - 55:ptr + 1]
#             ptr = 0
#             for i in range(0, 56, 7):
#                 digit = line[i:i + 7]
#                 if digit == '0000000':
#                     continue
#                 else:
#                     for k in range(10):
#                         if digit == digits[k]:
#                             decode[ptr] = k
#                             ptr += 1
#
#     if not (3 * (decode[0] + decode[2] + decode[4] + decode[6]) + decode[1] + decode[3] + decode[5] + decode[7]) % 10:
#         ans = sum(decode)
#
#     print(f'#{tc} {ans}')
#++++++++++===================================
decryption = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
         '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

def find(arr):
    global N, M, data
    for y in range(N):
        for x in range(M-1, -1, -1):
            if arr[y][x] == '1':
                data = arr[y][x-55:x+1]
                return data

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    data = ''
    find(arr)

    result = []
    start_i = 0
    end_i = 6
    for _ in range(8):
        result.append(decryption[data[start_i:end_i+1]])
        start_i += 7
        end_i += 7

    value = (result[0] + result[2] + result[4] + result[6])*3 + \
            (result[1]+result[3]+result[5]) + result[7]

    if not value % 10:
        print(f"#{tc} {sum(result)}")
    else:
        print(f"#{tc} 0")