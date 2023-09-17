numbers = list(map(int,input().split()))
k = int(input())
cache = {}
def dfs(i, count):
    if (i,count) in cache:
        return cache[(i,count)]
    if count == k:
        return 1
    if i == len(numbers):
        return 0
    res = numbers[i] * dfs(i+1, count+1) + dfs(i+1, count)
    cache[(i,count)] = res
    return res 
print(dfs(0,0))

