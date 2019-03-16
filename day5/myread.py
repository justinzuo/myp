
if __name__ == '__main__':
    #只读状态
    mfile = open(r"C:\Users\筱阿玉\PycharmProjects\myp\day5\liu","r")
    # #read()读取文件数据
    mstr = mfile.read()
    print(mstr)

    #每次读取文件光标都会改变，所以在这里用seek()函数重新设置光标位置
    mfile.seek(0)
    #按行读取文件，返回str字符串
    nstr = mfile.readline()
    print(nstr)

    mfile.seek(0)
    #读取文件的全部数据，返回一个list列表
    mlist1 = mfile.readlines()
    print(type(mlist1))
    print(mlist1)

    mfile.seek(0)
    #测试文件是否可读取
    flag = mfile.readable()
    print(type(flag))
    print(flag)

    #list()将文件数据以list列表形式返回
    mlist2 = list(mfile)
    print(type(mlist2))
    print("mlist2-->",mlist2)

    #tell()函数会查找当前的光标位置，返回int型
    num = mfile.tell()
    print(type(num))
    print(num)
    mfile.close()
