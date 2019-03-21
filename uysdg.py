def num():
    s = int(input("Input size:"))
    return s


a = [0, 0, 1]
k, j, i = a
for m in range(3, num()):
    a.append(i + k + j)
    k, j, i = j, i, i + k + j
print(a)
