def transform(matrix, encryption,length):
    result = []
    for i in range(length):
        total = 0; 
        for j in range(length):
            total += (matrix[j] * encryption[i][j])
        result.append(total % 37)
    return result
def getKey(val,map):
    for key, value in map.items():
        if val == value:
            return key
    return "-1"

n = int(input())
encryption = [list(map(int, input().split())) for i in range (n)]
message = input()
for i in range(n-len(message)%n):
    message+=' '
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
map = {letters[i]: i for i in range(len(letters))}
shift = [map.get(message[i]) for i in range(len(message))]
result = []
i=0
for i in range(n, len(shift)+1, n):
    
    result.append(transform(shift[i-n:i], encryption, n))
    
str = ''
for i in range(len(result)):
    for j in range(n):
        str+=getKey(result[i][j],map)
print(str)

