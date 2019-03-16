# 1.	编写Python程序判断字符串是否重复。（50分）
# 2.	编写Python程序打印输出字符串中重复的所有字符。（50分）
if __name__ == '__main__':
    mstr = input("请输入一个字符串")
    ndict = ""
    for i in mstr :
        if ndict.find(i)<0 :
            ndict+=i
            num = mstr.count(i)
            if mstr.count(i)>1:
                print("{son}重复了{num}次".format(son =i,num =num))
    mlist = ["huluwa","dawa","erwa"]
    qlist = mlist[0:]
    nlist = mlist
    #输出id值
    print("nlist.id-->",id(nlist),"mlist.id-->",id(mlist),"qlist.id-->",id(qlist))
    #输出全值
    print("nlist",nlist,"mlist",mlist,"qlist",qlist)
    #制定删除索引
    del qlist[0]
    print("qlist",qlist)
    #删除整个列表
    del qlist

if __name__ == '__main__':
    mlist = [5,3,6,94,9,8,7,1]
    mlist.sort()