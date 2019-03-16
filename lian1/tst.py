if __name__ == '__main__':
    klist = [
    "good ","good ","study",
    " good ","good","study ",
    "good "," good"," study",
    " good ","good"," study ",
    "good ","good ","study",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up"]

    nlist = []

    #for循环遍历klist列表数据
    for k in klist :
        nlist.append(k.strip())
    print("nlist-->",nlist)

    #创建set集合
    mset = set()
    for n in nlist :
        mset.add(n)
    print("mset-->",mset)

    #创建字典
    mdict = {}
    for i in mset :
        #存入键值对
        mdict[i]=nlist.count(i)
    print("mdict-->",mdict)
    for k,v in mdict.items() :
        print("{0}出现了{1}次".format(k,v))

    mstr = [" day day "," day day "]
    #只能除掉字符串的前后空白符，而不能除掉中间的空白符
    nstr = mstr[0].strip()
    print("nstr-->",nstr)