import random
def bingji() :
    qlist = [ random.randint(1,30) for i in range(1,16) ]
    plist = [ random.randint(1,30) for i in range(1,11) ]
    #求出并集返回给一个新的列表
    qset = { i for i in qlist }
    pset = { i for i in plist }
    nset = qset | pset
    print("qlist-->",qlist)
    print("plist-->",plist)
    print("qlist列表与plist列表的并集-->",nset)

def huiwen ():
    mstr = input("请输入一串字符:")
    nstr = mstr[::-1]
    print("mstr-->",mstr)
    print("nstr-->",nstr)
    #判断两个字符串是否相等
    if mstr == nstr :
        print("{0}是回文数".format(mstr))
    else:
        print("{0}不是回文数".format(mstr))

if __name__ == '__main__':
    bingji()
    huiwen()