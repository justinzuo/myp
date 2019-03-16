import random
if __name__ == '__main__':
    son1 = int(input("请输入第一个人的生日月份:"))
    son2 = int(input("请输入第二个人的生日月份:"))
    if son1>son2 :
        mo = son1%son2
        if mo == 1 :
            print("非常有缘")
        elif mo == 2 :
            print("比较有缘")
        elif mo == 3 :
            print("缘分一般")
        elif mo == 4 :
            print("有仇")
    else :
        mo = son2%son1
        if mo == 1 :
            print("非常有缘")
        elif mo == 2 :
            print("比较有缘")
        elif mo == 3 :
            print("缘分一般")
        elif mo == 4 :
            print("有仇")
    mlist = [ random.randint(1,15) for i in range(1,11) ]
    print(mlist)
