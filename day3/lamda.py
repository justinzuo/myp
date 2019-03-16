
def ling (a):
    b = a
    c = a
    for i in range(1,a+1) :
        print(" "*(b-1),"*"*(2*i-1))
        b-=1
    if i==a :
        for y in range(1,a) :
            print(" "*y,"*"*(2*c-3))
            c-=1

if __name__ == '__main__':
    mdict = {}
    username = input("请输入用户名:")
    password = input("请输入密码:")
    mdict[username]=password
    print(mdict)
    mstr = "lajiwanyi"
    #默认总左边开始分割，分割指定字符的前后位置,只分割一次
    nstr = mstr.partition("a")
    print(nstr)
    de="格".join(mstr)
    print(de)
