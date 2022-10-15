from os import remove


i, j = map(int, input().split())
map = {}
list = []
for x in range(i):
    list.append("T" + str(x+1))
    
for z in range(j): 
    line = input().split()
    if list.index(line[0]) > list.index(line[1]):
        list.remove(line[1])
        list.insert(list.index(line[0])+1, line[1])
        
print(' '.join(list))


