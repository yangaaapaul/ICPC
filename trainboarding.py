from collections import Counter
from math import modf


x,y,z = map(int, input().split())
loc = [int(input()) for i in range(z)]
dist = 0
map = Counter()
for i in loc:
    map[i//y + 1]+=1
    dist = max(dist, abs((i//y + 0.5) * y - i))
    print(abs((i//y + 0.5) * y - i))
print(round(dist))
print(map.most_common(1)[0][1])