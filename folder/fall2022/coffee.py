n = int(input())
line = input()
res = 0
cups = 0
for i in range(len(line)):
    if(line[i] == '1'):
        res+=1
        cups = 2
    else:
        if cups > 0:
            res+=1
            cups-=1

print(res)
