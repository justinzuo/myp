if __name__ == '__main__':
    mlist = input("请输入一个字符串")
    #len()函数返回指定字符串的长度
    mlen = len(mlist)
    print(mlen)
    if mlen<15:
        print("这个字符不够长")
    else :
        print("这个字符还行吧")

    mset = {"151","ada","qwer","dfaf"}
    #求mset的长度
    num = len(mset)
    print("mset的长度为-->",num)

    #创建一个元组
    mtuple = ("asd","pwd","aike")
    print("输出元祖",mtuple)
    num = len(mtuple)
    print(num)        #set,tuple,dict 都可以用len()函数求长度

    mstr = "1989-zxc-369"
    #分割字符串，字符串分割之后会返回一个列表
    nstr = mstr.split("-")
    print("分割后返回的列表-->",nstr,type(nstr))
    print("不会改变源字符串-->",mstr)
    lstr = "1989"
    b = "zxc" in nstr
    print(b)