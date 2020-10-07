for tc in range(1, int(input())+1):
    # 오만 / 만/  오천/ 천/ 오백/ 백/ 오십 / 십
    N = int(input())

    fiftythousand = N // 50000
    N = N - ( (N // 50000) * 50000 )
    tenthousand = N // 10000
    N = N - ( (N // 10000) * 10000 )
    fivethousand = N // 5000
    N = N - ( (N // 5000) * 5000 )
    thousand = N // 1000
    N = N - ((N // 1000) * 1000)
    fivehundred = N // 500
    N = N - ((N // 500) * 500)
    hundred = N // 100
    N = N - ((N // 100) * 100)
    fifty = N // 50
    N = N - ((N // 50) * 50)
    ten = N // 10
    N = N - ((N // 10) * 10)

    print(f"#{tc}")
    print(f"{fiftythousand} {tenthousand} {fivethousand} {thousand} {fivehundred} {hundred}"
          f" {fifty} {ten}")



