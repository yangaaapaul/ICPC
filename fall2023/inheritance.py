P = int(input())
res = [] 
def dfs(kids):
    if kids > P:
        return 
    if kids != 0 and P % kids == 0:
        res.append(kids)
    dfs(kids * 10 + 2)
    dfs(kids * 10 + 4)
dfs(0)
for num in sorted(res):
    print(num)