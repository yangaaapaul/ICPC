from re import M


list = [input().split() for i in range(int(input()))]
map = {}
for i in range(len(list)):
    for j in range(3):
        if j != 0:
            map[list[i][j]] = map.get(list[i][j],0)+1
count = 0
print(map)
for key, value in map.items():
    if(value==2):
        count+=1
print(count if count%3==0 else 'No trades possible')