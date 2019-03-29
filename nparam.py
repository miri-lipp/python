def gen(s):
    k, j, i = 0, 0, 1
    for m in range(3, s):
        k, j, i = j, i, i + k + j
        yield i + j + k


if __name__ == '__main__':
    filein = open(input("Name of input file "), "r")
    n = int(filein.readline())
    filein.close()
    l = [0, 0, 1]
    for a in gen(n):
        l.append(a)
    fileout = open(input("Name of output file "), "w+")
    fileout.write(str(l))
fileout.close()
