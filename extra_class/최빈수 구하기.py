T= int(input())
for tc in range(1, T+1):
    N = int(input())
    student = list(map(int, input().split()))
    score = [0] * 101
    for i in student:
        score[i] += 1

    maxV = 0
    for j in range(len(score)):
        if score[j] >= maxV:
            max_index = j
            max = score[j]
            maxV = max


    print(f'#{tc} {max_index}')

#+==============================================================
# 2
for tc in range(1, T+1):
    N = int(input())
    score_list = list(map(int, input().split()))
    score_dict = {}
    score_list.sort()
    for i in range(0, len(score_list)-1):
        score = score_list[i]
        if score in score_dict:
            score_dict[score] += 1
        else:
            score_dict[score] = 1

    max_count = 0
    result = 0
    for i in score_dict:
        if score_dict[i] >= max_count:
            max_count = score_dict[i]
            result = i

    print(f"#{tc} {result}")