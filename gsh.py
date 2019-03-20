x = []
j = int(input("Input number"))
while not int(j) == 0:
    mod = j % 16
    mod = int(mod)
    j = j/16
    if mod < 10:
        x.append(mod)
    elif mod == 10:
        k = "A"
        x.append(k)
    elif mod == 11:
        k = "B"
        x.append(k)
    elif mod == 12:
        k = "C"
        x.append(k)
    elif mod == 13:
        k = "D"
        x.append(k)
    elif mod == 14:
        k = "E"
        x.append(k)
    elif mod == 15:
        k = "F"
        x.append(k)
for i in reversed(x):
    print(i, end='')

##print(hex(b))