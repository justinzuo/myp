if __name__ == '__main__':
    mlist = {"sji","sda","c"}
    #update添加会以单个字符添加至集合
    mlist.update("我不知道")
    #add函数会将整个参数当成一个字符串添加进集合
    print(mlist)
    qlist = [ i for i in mlist]
    print(qlist)

    nlist = [i**2 for i in range(1,11)]
    print("列表：{nlist}".format(nlist=nlist))
    #上面等同于下面
    nlist=[]
    for i in range(1,11) :
        nlist.append(i**2)
    print("列表：{nlist}".format(nlist=nlist))
    #笛卡尔积
    qlist = ["bugai","shuxinsao","wenyanwen"]
    plist = [1,2,3]
    nlist = [str(m)+n for m in plist for n in qlist]
    print(nlist)
    nlist = [str(m) + n for m in plist for n in qlist if m%2!=0]
    print(nlist)

def ti1():
    mlist = []
    for i in range(1,11):
        mlist.append(i)
    return mlist
def ti2():
    mlist = []
    for i in range(11,21):
        mlist.append(i)
    return mlist
if __name__ == '__main__':
    mlist = ti1()+ti2()
    print("mlist-->",mlist)