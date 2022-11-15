import random
from random import sample, randint

arr =['R', 'O', 'Y', 'G', 'B', 'I', 'V']
count = 1
def write(n, line):
    global count
    print ("cat > secret%02d.in << EOF" % (count))
    count += 1
    print (n)
    print(line)
    print ("EOF")

def makerandomline():
    n = randint(1,100000)
    line =  " ".join([random.choice(arr) for _ in range(n)])
    write(n,line)

#creates 10 random tests
for _ in range(10):
    makerandomline()

#special case 1
n1 = 16
line1 = " ".join(["R", "R", "R", "R", "O", "O", "O", "O", "Y", "Y", "Y", "Y", "G", "G", "G", "G"])
write(n1, line1)

#special case 2
n2 = 2
line2 = " ".join(["R"])
write(n2, line2)

#special case 3
n3 = 1
line3 = " ".join(["R", "G"])
write(n3, line3)