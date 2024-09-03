from collections import defaultdict, deque
n = int(input())
mp = defaultdict(list)
in_degree = defaultdict(int)
nodes = set()
for i in range(n):
    line = input().split()
    file = line[0][:-1]  # Remove colon
    nodes.add(file)
    in_degree[file] = in_degree.get(file, 0)
    
    for dep in line[1:]:
        mp[dep].append(file)
        nodes.add(dep)
        in_degree[file] += 1
        
q = deque()

for node in nodes:
    if in_degree[node] == 0:
        q.append(node)

visited = set()
order = [] 
while q:
    node = q.popleft()
    if node in visited:
        continue
    visited.add(node)
    order.append(node)
    
    for dependent in mp[node]:
        in_degree[dependent] -= 1
        if in_degree[dependent] <= 0:
            q.append(dependent)

q.append(input())
visited = set()
while q:
    node = q.popleft()
    if node in visited:
        continue
    visited.add(node)
    for dependent in mp[node]:
        q.append(dependent)

for node in order:
    if node in visited:
        print(node)

