if __name__ == '__main__':
    #拼接列表
    qlist = [123,456,789]
    plist = ["abc","def","ghi"]
    #在创建一个列表
    nlist = []
    #开始拼接
    nlist = qlist+plist
    print("nlist-->",nlist)
    #判断某子串是否在列表内
    b = "de" in nlist
    print("n的值",b)
    if b :
        print("存在")
    else :
        print("不存在")

    wstr = input("请输入一个字符串:")
    #创建一个set集合
    mset = set()
    # 将wstr添加至set集合
    for i in wstr :
        mset.add(i)
    # 判断wstr字符串是否有重复的
    if len(wstr)!=len(mset) :
        print("mset有重复的字符")
    else :
        print("wstr里没有重复的字符")
    mset.update("gai")
    print(mset)