def helper(offset, everyone):
    teams = [[],[]]
    teamNumber, index = 0,0
    while everyone: 
        index = (index + offset) % len(everyone)
        teams[teamNumber].append(everyone.pop(index))
        teamNumber = (teamNumber + 1)%2
    return teams

bruh = helper(len(input().split())-1, [input() for i in range(int(input()))])
print(len(bruh[0]))
print('\n'.join(bruh[0]))
print(len(bruh[1]))
print('\n'.join(bruh[1]))

