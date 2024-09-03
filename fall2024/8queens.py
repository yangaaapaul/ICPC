import sys
data = sys.stdin.readlines()
board = [list(line.strip()) for line in data]
m,n = len(board), len(board[0])
visited = set()
def check():
    for i in range(m):
        for j in range(n):
            if board[i][j] == "*":
                if i in visited or -j in visited:
                    return False
                visited.add(i)
                visited.add(-j)
    starts = [(i,0) for i in range(m) ] + [(0,i) for i in range(n)]
    for x,y in starts:
        x1,y1 = x,y
        x2,y2 = x,y
        while 
            
