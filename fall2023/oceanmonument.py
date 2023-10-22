from functools import cache
@cache
def dfs(g, eg):
    if g <= 1 and eg == 0: 
        return 1
    count = 0 
    if g > 1:
        count+= 1 + dfs(g-1, eg)
    else:
        count+= 1 +  dfs(g+1, eg-1)
    return count
    
for i in range(int(input())):
    g,eg = map(int, input().split())
    print(dfs(g,eg))