import random
def day ():
    print("第一题")
    # 输入某年某月某日，判断这一天是这一年的第几天？
    birthday = input("请输入年月日，格式为××××-××-××:")
    # 现将字符串进行切割
    num = 0
    year = ""
    month = ""
    date = ""
    for i in birthday:
        if num == 0:
            if i == "-":
                num += 1
            else:
                year += i
        elif num == 1:
            if i == "-":
                num += 1
            else:
                month += i
        elif num == 2:
            if i == "-":
                num += 1
            else:
                date += i
    # 输出年，月，日
    print("{year}年{month}月{date}日".format(year=year, month=month, date=date))
    # 将年月日字符串转化为int类型
    year = int(year)
    month = int(month)
    date = int(date)
    # 创建一个字典
    mdict1 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    mdict2 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31, }
    print(mdict1)
    print(mdict2)
    # 判断是否是闰年
    day = 0
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        # 循环已经过去的月数
        for i in range(1, month):
            day += mdict1[i]  # 将已经过去的天数添加至day
        day = day + date
    else:
        # 循环已经过去的月数
        for i in range(1, month):
            day += mdict2[i]  # 将已经过去的天数添加至day
        day = day + date
    print("这是{year}年的第{day}天".format(year=year, day=day))

def yuan():
    print("第二题")
    # 第二题:输入两个人的出生月份，来计算两个人的缘
    mon1 = int(input("请输入第一个人的月份:"))
    mon2 = int(input("请输入第二个人的月份:"))
    if mon1 > mon2:
        if mon1 % mon2 == 1:
            print("非常有缘")
        elif mon1 % mon2 == 2:
            print("比较有缘")
        elif mon1 % mon2 == 3:
            print("缘分一般")
        elif mon1 % mon2 == 4:
            print("有仇")
    else:
        if mon2 % mon1 == 1:
            print("非常有缘")
        elif mon2 % mon1 == 2:
            print("比较有缘")
        elif mon2 % mon1 == 3:
            print("缘分一般")
        elif mon2 % mon1 == 4:
            print("有仇")
        else :
            print("月份相等了")

def suiji():
    print("第三题")
    #随机生成列表
    mlist = []
    for i in range(1,10):
        mlist.append(random.randint(1,100))
    num = random.randint(1,100)
    print("mlist-->",mlist)
    print(num)
    flag = False
    #判断这个整数是否在列表中存在
    for i in mlist :
        if num==int(i) :
            flag = True
            break
    if flag :
        print("{0}存在mlist中".format(num))
    else :
        print("{0}不存在mlist中".format(num))

def pai ():
    print("第四题")
    #随机生成一个列表
    mlist = [ random.randint(1,100) for i in range(1,11) ]
    print("原列表{0}".format(mlist))
    print("排序后：")
    #队列表进行排序
    mlist.sort() #默认升序
    nlist = sorted(mlist) #对列表进行临时排序返回一个新列表
    print("mlist-->",mlist)
    print("nlist-->",nlist)
    #冒泡排序
    for i in range(0,len(mlist)) :
        for j in range(0,len(mlist)-i-1) :
            if mlist[j]>mlist[j+1] :
                lem = mlist[j]
                mlist[j]=mlist[j+1]
                mlist[j+1]=lem
    print("mlist-->",mlist)