import math

My_list = [*range(1000000,100000000, 1)]
#print(My_list)
g = 0
a = 0
d = 0
b = My_list[a]
cupok = []
L = max(My_list)
    
while a < L:
    b = My_list[a]
    print(str(b) + "b")
    f = int(math.log10(b)+1)
    while d < f:
        c = (int(str(b)[d]))
        g += c**f
        d += 1
    if g == b:
        cupok.append(b)
        d = 0
        g = 0
        print("kilop")
    else:
        d = 0
        g = 0
    a += 1
print(cupok)