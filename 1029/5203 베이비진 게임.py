T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    win = 0
    for i in range(len(arr)):
        # player1
        if i % 2 == 0:
            player1[arr[i]] += 1
        #plyaer2
        elif i % 2 != 0:
            player2[arr[i]] += 1
        #player1
        if max(player1) > 0:
            # run
            for j in range(len(player1) - 2):
                if player1[j] > 0 and player1[j+1] > 0 and player1[j+2] > 0:
                    win = 1
                    break
            # triplet
            for j in range(len(player1)):
                if player1[j] == 3:
                    win = 1
                    break
        #player2
        if max(player2) > 0:
            for j in range(len(player2) - 2):
                if player2[j] > 0 and player2[j+1] > 0 and player2[j+2] > 0:
                    win = 2
                    break
            # triplet
            for j in range(len(player2)):
                if player2[j] == 3:
                    win = 2
                    break

        if win == 1:
            break

        if win == 2:
            break
    print("#{} {}".format(tc, win))
