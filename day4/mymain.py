import day4.quest1.p1 as p1

#主函数
if __name__ == '__main__':
    mdict = {1:"{1}查看第一题",
             2: "{2}查看第二题",
             3: "{3}查看第三题",
             4: "{4}查看第四题"
    }
    mdictfun = {1:p1.check,
                2:p1.bingji,
                3:p1.user,
                4:p1.huiwen
    }
    while True :
        for v in mdict.values() :
            print(v)
        chose = int(input("请输入选择:"))
        mdictfun[chose]()
        # if chose == 1 :
        #     p1.check()
        # elif chose == 2 :
        #     p1.bingji()
        # elif chose == 3 :
        #     p1.user()
        # elif chose == 4 :
        #     p1.huiwen()
        # else :
        #     print("识别不了您的选择！")
