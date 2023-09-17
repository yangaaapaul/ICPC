from functools import cache 
r,c = map(int,input().split())
matrix = [list(map(int,input())) for i in range(r)]
n = int(input())
@cache
def dfs(x1,y1,x2,y2,dig):
    if x1 == x2 and y1 == y2: 
        return True
    if x1 >= r or x1 < 0 or y1 >=c or y1 < 0 or matrix[x1][y1] != dig or matrix[x1][y1] == -1:
        return False
    temp = matrix[x1][y1]
    matrix[x1][y1] = -1
    res= dfs(x1+1,y1,x2,y2,dig) or dfs(x1,y1+1,x2,y2,dig) or dfs(x1-1,y1,x2,y2,dig) or dfs(x1,y1-1,x2,y2,dig)
    matrix[x1][y1] = temp
    return res

for i in range(n):
    points= list(map(int,input().split()))
    r1,c1,r2,c2 = points[0] -1, points[1]-1,points[2]-1,points[3]-1
    bin = dfs(r1,c1,r2,c2,matrix[r1][c1])
    dec = dfs(r2,c2,r1,c1,matrix[r2][c2])
    if bin and dec: print("decimal")
    elif bin: print("binary")
    else: print("neither")

   

