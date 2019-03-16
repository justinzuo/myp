#创建列表
if __name__ == '__main__':
    #创建列表并存入偶数
    mlist = [i for i in range(0,10) if i%2==0]
    print(mlist)
    mlist2 = ["list","set","query","die"]
    #利用循环创建列表
    mlist3 = [ i for i in mlist2 ]
    print("mlist3->",mlist3)