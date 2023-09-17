

n = int(input())
encryption = [list(map(int, input().split())) for i in range (n)]
message = input()
rem = len(message) % n
if rem > 0: 
    message = message + ' ' * (n-rem)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
map = {letters[i]: i for i in range(len(letters))}
result = []

for i in range(len(message)//n):   
    chunk = message[n*i:n*(i+1)]
    x = [map[l] for l in chunk]
    for j in range(n):
        result.append(letters[sum(encryption[j][k] * x[k] for k in range(n) ) %37])
print("".join(result))

