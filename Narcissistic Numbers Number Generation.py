My_list = [*range(100, 1000, 1)]
print(My_list)

f = 3
a = 0
b = My_list[a]
cupok = []

    
while a<900:
    b = My_list[a]
    c = (int(str(b)[0]))
    d = (int(str(b)[1]))
    e = (int(str(b)[2]))
    a = a + 1
    g = (c)**3 + (d)**3 + (e)**3
    print(b)
    if g == b:
        cupok.append(b)
    else:
        continue

print(cupok)