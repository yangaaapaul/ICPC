#!/usr/bin/python3




from collections import defaultdict


n = int(input())
C = input().split()

def max_len(arr):
    map = defaultdict()
    l, r = 0,0
    left, right = 0,0
    maxi = 2
    if len(arr) <=2:
        return len(arr)
    for i in range(len(arr)):
        map[arr[r]] = r
        r+=1
        if len(map) == 3:
            if r-l > maxi:
                maxi = r-l
                left, right = l, r-1
            idx = min(map.values())
            del map[arr[idx]]
            l = idx + 1
            
    return C[left:right]

print(max_len(C))
    



