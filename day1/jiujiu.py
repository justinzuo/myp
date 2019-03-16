if __name__ == '__main__':
    i = 1
    c = '*'
    h = '='
    while i<=9 :
        j = 1
        while j<=i :
            ji = i*j
            print("{0}{1}{2}{3}{4}".format(i, c, j, h, ji), end=" ")
            j+=1
        print("\n")
        i+=1