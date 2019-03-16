if __name__ == '__main__':
    mstr = input("请输入一个字符串:")
    mset = set()
    for i in mstr:
        mset.add(i)
    if len(mstr)!=len(mset):
        print("重复了")
        mdict = {}
        for i in mset:
            if mstr.count(i)>1:
                mdict[i] = mstr.count(i)
        for k,v in mdict.items():
            print("{0}重复了{1}次".format(k,v))
    else:
        print("没有重复")
#3.	#把下面的klist作为字典的键
#同时作为字典的值

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
        " day ","day"," up"
                            ]
    #创建字典
    ndict = {k.strip():k.strip() for k in klist}
    print("字典ndict：{ndict}".format(ndict=ndict))

     # 把下面的klist作为字典的键
    # 并统计每个单词的词频
    vlist = [ i.strip() for i in klist ]
    mset = { i for i in vlist }
    print("集合mset：{mset}".format(mset=mset))
    ndict = {k.strip():vlist.count(k) for k in mset }
    print("字典ndict：{ndict}".format(ndict=ndict))

    print(input("请写出一首诗"))