if __name__ == '__main__':
    #实现循环5次，步长为3,三个整形参数，
    # 第一个参数小于第二个参数时第三个参数不能为负数
    #第一个参数不小于第二个参数时，第三个参数不能为正数
    for i in range(1,9,3) :
        print(i)
    #参数为负数时
    print("负数")
    for i in range(9,1,-3) :
        print(i)

if __name__ == '__main__':
    #使用range初始化一个列表
    mlist = [ i for i in range(0,10,1)]
    print(mlist)
    # 使用range初始化一个列表
    mlist = [i for i in range(10, 0, -1)]
    print(mlist)