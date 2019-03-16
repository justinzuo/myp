
if __name__ == '__main__':
    with open(r"C:\Users\筱阿玉\PycharmProjects\myp\day5\liu","w+") as mfile :
        mstr = input("请输入:")
        #mfile()想括号里直接写入字符串，就会向文件中添加并返回添加的字符个数
        num = mfile.write(mstr)
        print(num)
        mstr = input("在此写入:")

        #writelines()向文件写入多行，返回值None
        num = mfile.writelines(mstr)
        print(num)

        #writable()函数会测试文件是否可写,返回一个布尔值
        flag = mfile.writable()
        print(type(flag))
        print(flag)

        #设置光标位置，再进行写入
        mfile.seek(3)
        mstr = input("请输入:")
        num = mfile.writelines(mstr)
        print(num)

        mlist = mfile.readlines()
        print(mlist)