
def ling (a):
    #菱形
    b = a
    c = a
    for i in range(1,a+1) :
        print(" "*(b-1),"*"*(2*i-1))
        b-=1
    if i==c:
        for y in range(1,a) :
            print(" "*y,"*"*(2*c-3))
            c-=1

def sanjiao(a):
    b = a
    for i in range(1,a+1) :
        mstr = " "*(b-1)
        nstr = "* "*i
        print("{0}{1}".format(mstr,nstr))
        b-=1

def jiujiu () :
    for i in range(1,10) :
        for j in range(1,i+1) :
            print("{0}*{1}={2}".format(j,i,i*j),end=" ")
        print("\n")

def right () :
    for i in range(1,101) :
        print(str(i).rjust(3,"-"),end=" ")
        if i%10==0 :
            print("\n")
