from sys import stdin 
import math 
while True: 
    try:
        num = int(input())
        summ = 1
        x = int(math.sqrt(num))
        if math.sqrt(num) == math.ceil(math.sqrt(num)):
            summ -= x
        for p in range(2,x + 1):
            if num % p == 0:
                summ += p + (num // p)
        if summ == num:
            print(f'{num} perfect')
        elif abs(num - summ) <= 2:
            print(f'{num} almost perfect')
        else:
            print(f'{num} not perfect')
    except EOFError:
        break
    except ValueError:
        pass