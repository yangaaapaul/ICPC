from collections import defaultdict
mp = defaultdict(int)
maxi = 0 
while True:
    person = input()
    if person == "***":
        break
    mp[person]+=1
    maxi = max(maxi,mp[person])
res = [k for k,v in mp.items() if v == maxi]
print(res[0] if len(res) == 1 else "Runoff!")