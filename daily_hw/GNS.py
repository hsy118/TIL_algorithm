# T = int(input())
# key_str = {}
# sample = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# for key, value in enumerate(sample):
#     key_str[value] = key
# key_num = {}
# for key, value in enumerate(sample):
#     key_num[key] = value
#
# for tc in range(1, T+1):
#     t, N = input().split()
#     arr = list(input().split())
#     num_result = []
#     str_result = []
#     for i in arr:
#         num_result.append(key_str[i])
#
#     num_result.sort()
#
#     for i in num_result:
#         str_result.append(key_num[i])
#     answer = ' '.join(str_result)
#     print(f'#{tc}\n{answer}')
#------------------------------------------------------------
# T = int(input())
# sample = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# for tc in range(1, T+1):
#     t, N = input().split()
#     arr = list(input().split())
#     counting_list = [0] * 10
#     for i in arr:
#         if i in sample:
#             counting_list[sample.index(i)] += 1
#     answer=""
#     for i in range(len(counting_list)):
#         answer += ((sample[i]+' ') * counting_list[i])
#     print(answer)
#+++++++++++++++++++++++++++++++++++++++++++
T = int(input())
sample = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dict1 = {i : 0 for i in sample}
for tc in range(1, T+1):
    dict1 = {i: 0 for i in sample}
    t, N = input().split()
    arr = list(input().split())
    for i in arr:
        if i in dict1:
            dict1[i] += 1
    answer =''
    for i in dict1:
        answer += (i + ' ') * dict1[i]
    print(f'#{tc}\n{answer}')
