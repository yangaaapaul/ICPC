from collections import Counter


def solve():
    last = input()
    n = int(input())
    valid = []
    map = Counter()
    for _ in range(n):
        guess = input()
        if guess[0] == last[-1]:
            valid.append(guess)
        map[guess[0]] += 1

    for x in valid:
        map[x[0]] -= 1
        if map[x[-1]] == 0:
            print(f'{x}!')
            return
        map[x[0]] +=1
    print("?" if len(valid) ==0 else valid[0])
solve()
