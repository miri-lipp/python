a = [0, 0, 1]
s = int(input("Input size:"))
k, j, i = a
print("Tribonacci numbers:")
for m in range(3, s):
    a.append(i + k + j)
    k, j, i = j, i, i + k + j
print(a)
