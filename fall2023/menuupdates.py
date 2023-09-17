import heapq
mp,hp = {},[]
d,u = map(int,input().split())
mini = 1
for i in range(1,u+1):
    line = input().split()
    if line[0] == 'a':
        if hp:
            if i >= int(hp[0][1]) and i >= int(hp[0][0]):
                print(hp[0][0])
                heapq.heappop(hp)
            else:
                print(str(mini))
        else:
            print(str(mini))
        mini+=1
            
    else:
        heapq.heappush(hp,(line[1],i+d))