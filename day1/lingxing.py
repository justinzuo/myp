if __name__ == '__main__':
    a = int(input(">>>"))
    c = a
    b = a
    for i in range(1, a + 1):
        print(" " * (c - 1), "*" * (2 * i - 1))
        c = c - 1
    if (i == a):
        for y in range(1, a):
            print(" " * y, "*" * (2 * b - 3))
            b = b - 1