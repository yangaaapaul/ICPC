from collections import defaultdict,deque
n,m = map(int,input().split())
edges = defaultdict(list)
for i in range(m):
    x,y = map(int,input().split())
    edges[x].append(y)
    edges[y].append(x)
q,visited = deque([(1,1)]),set([1])
def bfs():
    while q:
        node,leng = q.popleft()
        for edge in edges[node]:
            if edge == n:
                return leng
            if edge not in visited:
                visited.add((edge))
                q.append((edge,leng+1))
    return -1
print(bfs()-1)


