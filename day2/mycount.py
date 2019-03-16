if __name__ == '__main__':
    mstr = "deepdarkfantasies, 吼吼吼吼全给党"
    mlist = ""
    print(mstr)
    for i in mstr :
        num = mstr.count(i)
        find = mlist.find(i)
        if find<0 :
            mlist+=i
            if num>1 :
                print("重复的字符为:{0}\t重复了{1}次".format(i,num))
    print("---------------------------------------------------------")
    mset = set()
    for i in mstr :
        num = mstr.count(i)
        if num>1 :
            mset.add(i)
    for i in mset :
        num = mstr.count(i)
        print("重复的字符为:{0}\t重复了{1}次".format(i,num))

    mdict = {}

    klist = ["name","age","password"]
    for k in klist :
        mdict[k] = k
    print("mdict-->",mdict)

    #判断输入的年是否为闰年
    nian = int(input("请输入一个年数"))
    if nian%4==0 and nian%100!=0 or nian%400==0:
        print("{0}年是闰年".format(nian))
    else :
        print("{0}年不是是闰年".format(nian))