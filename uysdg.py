def gen(s):
    k, j, i = 0, 0, 1
    for m in range(3, s):
        k, j, i = j, i, i + k + j
        yield i + j + k


if __name__ == '__main__':
    m = [0, 0, 1]
    s = int(input("Input size:"))
    for a in gen(s):
        m.append(a)
    print(m)

