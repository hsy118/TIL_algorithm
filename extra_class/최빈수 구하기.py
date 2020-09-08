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

