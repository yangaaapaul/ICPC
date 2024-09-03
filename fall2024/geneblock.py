dirtblocks = [int(input()) for i in range(int(input()))]

for d in dirtblocks:
    res = 0
    while d > 7 and d % 10 != 7:
        d -= 7
        res += 1
    print(res + 1 if d % 10 == 7  else -1)
