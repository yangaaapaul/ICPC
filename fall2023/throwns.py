n,k = map(int, input().split())
commands = input().split()
i, s = 0,[]

while i < len(commands):
    if commands[i] == "undo":
        for j in range(int(commands[i+1])):
            if s: s.pop()
        i+=2
    else:
        s.append((int(commands[i])))
        i+=1
print(sum(s) % n)


