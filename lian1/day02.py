if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    #先设置一个空set集合
    mset = set()
    for k in klist :
        #将klist里的元素存入set集合
        k = k.strip()
        mset.add(k.strip())
    print("mset集合-->",mset)

    #创建空的字典
    mdict = {}
    #循环set集合对字典添加相应的键值对
    for k in mset :
        mdict[k]=klist.count(k)

    print("mdict字典-->",mdict)
    #在经过for循环详细输出字符出现的词频
    for k,v in mdict.items() :
        mstr = "{0}出现了{1}次".format(k,v)
        print(mstr.rjust(15,"-"))

    # mstr = "goingcamebacksleep"
    # lset = set()
    # for i in mstr :
    print("--------------------------")
    print("第一中方法")
    mstr = "www.baiwei.com"
    nstr = ""
    for i in mstr :
        num = mstr.count(i)
        ct = nstr.find(i)
        if ct<0 and num>1:
            nstr+=i
            print("{0}重复了{1}次".format(i,num))
    print("------------------第二种方法------------------")
    nstr = ""
    for  i in mstr :
        mlist = mstr.split(i)
        num = len(mlist)-1
        if nstr.find(i)<0 :
            nstr+=i
            if num > 1:
                print("{0}重复了{1}次".format(i, num))