if __name__ == '__main__':
    mdict = {"username":15,"password":123}
    #打印类型
    print(type(mdict))
    for k,v in mdict.items():
        print("mdict->{0}={1}".format(k,v))

    #创建字典
    ndict = { k:v for k,v in mdict.items() }
    print(ndict)
    #        默认获取的是键
    for k in ndict :
        print(k)
    #             获取值
    for k in ndict.values():
        print(k)
    #             获取键
    for k in ndict.keys():
        print(k)
    #向字典添加键值对
    adict = {}
    klist = ["1545","mysql","request"]
    vlist = ["liu","jid","de"]
    for k in klist :
        adict[k] = vlist[klist.index(k)]
    print(adict)

    qdict = {"name":"good","age":"18"}
    #添加键值对
    qdict["word"]="qwe"
    #修改值
    qdict["name"]="zhangsan"
    print(qdict)
    #删除键-值
    del qdict["name"]
    print(qdict)
    #删除整个字典
    del qdict

    bdict = {"name":"good","age":"18","sex":"男"}
    #求字典长度
    num = len(bdict)
    print("长度为：",num)
    print(type(bdict))
    #访问值
    for v in bdict:
        pass

