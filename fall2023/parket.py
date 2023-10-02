import math
R,B = map(int,input().split())
total = R + B
for L in range(1,int(math.sqrt(total)+1)):
    if total % L == 0:
        W = total // L
        if 2 * W + 2 * L -4 == R:
            print(f'{L} {W}' if L > W else f'{W} {L}')
            break 
