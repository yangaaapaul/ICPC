from collections import defaultdict
n = int(input())
mp = defaultdict(list)
for i in range(n):
    edges = input().split()
    for i in range(1,len(edges)):
        mp[edges[0]].append(edges[i])
        mp[edges[i]].append(edges[0])
start, end = input().split()
bruh = []
def dfs(start,end,path,visited):
    if start == end:
        bruh.append(path.copy()) 
        return
    for edge in mp[start]:
        if edge not in visited and not bruh:
            visited.add(edge)
            dfs(edge,end,path + [edge],visited)
            visited.remove(edge)
sett = set([start])
dfs(start,end,[start],sett)
print(" ".join(bruh[0]) if bruh else "no route found")
