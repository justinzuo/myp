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
    #创建vlist列表并初始化
    vlist = [ k for k in klist ]
    print(vlist)
    #创建空字典
    mdict = {}
    for v in vlist :
        #存入字典键值对
        mdict[v] = klist[vlist.index(v)]
    print(mdict)

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
        " day ", "day", " up"]
    vlist = []
    for k in klist :
        vlist.append(k.strip())
    print("vlist-->",vlist)
    #创建字典
    mdict = { k.strip():k.strip() for k in klist }
    for k in klist :
        #存入字典键值对
        mdict[k.strip()] = k.strip()
    print("mdict-->",mdict)