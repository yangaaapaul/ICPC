x,y,z = map(int, input().split())
for i in range(z):
    line = input().split()
    Found = False
    for num in line[1:]:
        if int(num) == y:
            Found =  True
            break
    print("Keep" if Found else "REMOVE")