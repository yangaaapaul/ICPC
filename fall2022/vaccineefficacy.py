
n = int(input())
cmap, map = {}, {}
for i in range(n):
    line = input()
    for j in range(0,4):
        if line[0] == 'Y':
            if line[j] == 'Y':
                map[j]  = map.get(j,0)+1
        else:
            if line[j] == 'Y':
                cmap[j]  = cmap.get(j,0)+1
print(map)
print(cmap)
for i in range(1,4):
    x = map.get(0)
    iNum = map.get(i) if map.get(i) != None else 0
    ir = (iNum / (x)) * 100
    cNum = cmap.get(i) if cmap.get(i) != None else 0
    cir = (cNum / (n-x)) * 100
    if ir > cir:
        print("Not Effective")
    else:
        diff = ((cir - ir) / cir) * 100 
        print(format(diff, '.6f'))
    
    
    