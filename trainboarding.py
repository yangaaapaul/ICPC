x,y,z = map(int, input().split())
train = [0] * x
maxWalk = 0
for i in range(z): 
    d = int(input())
    car = min(x-1, d//y)
    train[car] += 1
    maxWalk = max(maxWalk, abs((car * y + y//2) -d))
print(maxWalk)
print(max(train))