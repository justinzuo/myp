
if __name__ == '__main__':
    mstr = "hello world \n you are welcome \n fuck you mouses"
    print(mstr)
    #center()进行字符串居中,返回一个新字符串
    nstr = mstr.center(50,"-")
    print(nstr)

    #splitlines()进行字符串切割，按行(\n)进行切割返回一个列表
    nstr = mstr.splitlines()
    print(nstr)

    #在字符串中每一个字符中间都添加一个指定的字符,返回一个新的字符串
    mstr = "likeyoumylady"
    nstr = "o".join(mstr)
    print(nstr)

    #会将指定的字符在字符串中的第一次出现的前后位置进行切割,返回一个元组
    mstr = "weneedjodplease"
    nstr = mstr.partition("e")
    print(nstr)

    print(6^11)
