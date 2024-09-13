from collections import defaultdict

n, m = map(int, input().split())

roads = []
for i in range(m):
    x, y, dist = map(int, input().split())
    roads.append((dist, x, y))
roads.sort()

par = [i for i in range(n)]

def find(a):
    if a != par[a]:
        par[a] = find(par[a])  
    return par[a]

def join(a, b):
    para, parb = find(a), find(b)
    if para != parb:
        par[para] = parb  

mini = 0
flag = True
for dist, road1, road2 in roads:
    if find(road1) != find(road2):
        join(road1, road2)
        mini = max(mini, dist) 

for i in range(1, n):
    if find(i) != find(i-1):
        print("IMPOSSIBLE")
        flag = False
        break
if flag:
    print(mini)
