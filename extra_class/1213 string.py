for tc in range(1,11):
    t = int(input())
    word = input()
    arr = input()
    num_word = arr.count(word)
    print(f'#{tc} {num_word}')
#----------------------------------------
"""
이거 패턴 매칭 - brute force
"""
def find(text, pattern):
    global ans
    for i in range(len(text) - len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else: cnt += 1
        if cnt >= len(pattern):
            ans += 1


for tc in range(11):
    ans = 0
    no = input()
    pattern = input()
    text = input()
    find(text, pattern)
    print(f"{tc+1} {ans}")