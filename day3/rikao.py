import day3.quest1.p1 as p1
if __name__ == '__main__':
    #创建一个选择字典
    mdict = {1:"{1}计算天数",
             2:"{2}判断缘分",
             3:"{3}查看一个整数是否存在于一个列表",
             4:"{4}对列表进行排序",
             0:"{0}退出程序"}
    #将函数存入字典
    mdfun ={1:p1.day,
            2:p1.yuan,
            3:p1.suiji,
            4:p1.pai}
    #循环
    while True :
        for v in mdict.values():
            print("{0}".format(v))
        bh = int(input("请输入您的选择:"))
        if bh==0 :
            break
        else :
            mdfun[bh]()
        print("\n")
