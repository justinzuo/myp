if __name__ == '__main__':
    num = "10"
    nb = num.rjust(10,"-")
    print(nb)
    for i in range(1,10) :
        nstr = ""
        for j in range(1,i+1) :
            nstr="{0}*{1}={2}".format(j,i,i*j)
            print("{0}*{1}={2}".format(j,i,i*j).rjust(8,"-"),end=" ")
        print("\n")
    print("-------------------------------------------")
    for i in range(1,101) :
        num = str(i)
        print(num.rjust(3,"-"),end=" ")
        if i%10==0 :
            print("\n")