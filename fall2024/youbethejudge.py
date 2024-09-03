import sys
def prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
res = [] 
for line in sys.stdin.readlines():
    line = line.strip().split()
    for ch in line:
        try:
            if str(int(ch)) != ch:
                raise Exception
            res.append(ch)
        except: 
            print(0)
            sys.exit(0)
res = [int(x) for x in res]
print(int(len(res) == 3 and res[0] % 2 == 0 and res[0] > 3 and res[0] <= 10**9 and prime(res[1]) and prime(res[2]) and res[1] + res[2] == res[0]))