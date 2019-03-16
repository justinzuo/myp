
if __name__ == '__main__':
    #with语句可以避免已经打开的文件                                    别名
    with open(r"C:\Users\筱阿玉\PycharmProjects\myp\day5\liu","r+") as mfile :
        #list()将文件中的数据以行为单位转化为列表返回一个列表
        mlist = list(mfile)
        print(mlist)
        #read()读取文件的全部信息
        mstr  = mfile.read()
        print(type(mstr))
        print(mstr)
        mstr = input("请输入：")
        num = mfile.writelines(mstr)
        print(num)
        for i in range(1,5) :
            mstr = input("请输入:")
            num = mfile.writelines(mstr)


if __name__ == '__main__':
    with open(r"C:\Users\筱阿玉\PycharmProjects\myp\day5\liu","r") as mfile:
        mstr = mfile.read()
        mfile.seek(3)
        print(mstr)
        nstr = mfile.readline()
        print(nstr)
        mlist = mfile.readlines()
        nlist = list(mlist)
        print(mlist,nlist)

