n = int(input())
list = [int(input()) for i in range(n)]
if n%2 == 1:
    print('still running')
else:
    total = 0
    for i in range(1,len(list),2):
        total += (list[i] - list[i-1])
    print(total)