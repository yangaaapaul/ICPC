inp = input()
res = [] 
def dfs(i,path):
    res.append(path)
    if i == len(inp):
        return
    for j in range(i, len(inp)):
        dfs(j+1, path+ inp[j])
dfs(0,"")
print(sorted(res, key = len))
