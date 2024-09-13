n = int(input())
def parse():
    line = input().split()
    char = int(line[0] == "#")
    pixels = list(map(int, line[1:]))
    summ = sum(pixels)
    res = ""
    for num in pixels:
        if char:
            res += "#" * num
        else:
            res += "." * num
        char = (char+1) % 2
    
    return summ, res

while True:
    error = False
    summ, line = parse()
    print(line)
    for i in range(1, n):
        summ2, line2 = parse()
        print(line2)
        if summ != summ2:
            error = True
    
    if error:
        print("Error decoding image")
    n = int(input())
    if n != 0:
        print()
    else:
        break
