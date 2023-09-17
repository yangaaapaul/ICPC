n = int(input())
has = {}
wants = {}
for i in range(n):
    p, h, w = input().split()
    has[h] = p
    wants[p] = w
longest = 0
isCycle = False
for i in wants:
    s = i
    count =0
    while s in wants and wants[s] in has:
        s = has[wants[s]] 
        count += 1
        if s == i:
            isCycle = True
            break 
    if isCycle:
        longest = max(longest, count)
if longest > 0: 
    print(longest)
else: 
    print("No trades possible")