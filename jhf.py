b = []
g = int(input("Input size:"))
k = -1
for i in range(g):
    if i % 2 == 0:
        i = str(i)
        num = ''
        for j in i:
            num += i * 2
        b.append(num)
    else:
        if i // 10 == 0:
            b.append(k)
        elif not i // 10 == 0:
            i = i // 10
            b.append(i)
print(b)
