p1,p2 = list(map(int,input().split())), list(map(int,input().split()))
mp1,mp2 = set(),set()
for i in range(1,len(p1)):
    mp1.add(p1[i]) 
for i in range(1,len(p2)):
    mp2.add(p2[i])
days = 0
flag1,flag2 = True,True 
for i in range(0,1000000):
    if i in mp1 and i in mp2:
        flag1 = True
        flag2 = True
        days+=1
    elif i in mp1 and flag2:
        flag1 = True
        days+=1
        flag2 = False
    elif i in mp2 and flag1:
        flag2 = True
        days+=1
        flag1 = False
print(days)