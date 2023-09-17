from collections import defaultdict 
from sys import stdin 
p,t = map(int,input().split())
mp = defaultdict(list)
for line in stdin.readlines():
    i,j = map(int, line.split())
    mp[i].append(j)
sett = set()
for j in range(1,p+1):
    sett.add(",".join(str(i) for i in sorted(mp[j])))
print(len(sett))