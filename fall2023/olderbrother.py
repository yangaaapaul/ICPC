import math
def is_prime(n):
    if n == 1: 
        return False
    if n == 2: 
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())

def prime_power(q):
    if q == 1: 
        return False
    elif is_prime(n):
        return True
    else:
        for i in range(2, int(math.sqrt(q)+1)):
            if is_prime(i):
                k = 0 
                num = i 
                while q % i == 0 and num < q:
                    num*=i
                    k+=1
                if k > 0 and num == q:
                    return True
        return False
print("yes" if prime_power(n) else "no")
