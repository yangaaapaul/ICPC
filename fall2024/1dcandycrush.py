inp = input()
def crushable(inp):
    l,r = 0,0
    while r < len(inp):
        while r < len(inp) and inp[l] == inp[r]:
            r+=1
        if r - l >= 3:
            return (l,r)
        l = r
    return (0,0)

def crush(inp):
    l,r = crushable(inp)
    if (l,r) == (0,0):
        return inp
    return crush(inp[:l] + inp[r:])
print(crush(inp))
    
    