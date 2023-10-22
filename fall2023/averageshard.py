n = int(input())
for i in range(n):
    input()
    x,y = map(int,input().split())
    res = 0 
    cs = list(map(int,input().split()))
    econ = list(map(int,input().split()))
    cs_total, econ_total = sum(cs), sum(econ)
    cs_avg, econ_avg = cs_total/x, econ_total/y
    for student in cs: 
        new_cs = (cs_total - student)/(x-1)
        new_econ = (econ_total + student) / (y+1)
        if new_cs > cs_avg and new_econ > econ_avg:
            res+=1
    print(res)
    