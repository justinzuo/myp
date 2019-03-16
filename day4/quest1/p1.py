import  random
def check() :
    print("第一题")
    name = input("请输入姓名:")
    sex = input("请输入性别:")
    if sex == "男":
        mstr =  "先生"
    elif sex == "女" :
        mstr = "女士"
    mdict = {}
    mdict[name]=mstr
    for k,v in mdict.items() :
        print("{0}{1}欢迎您的到来".format(k,v))

def bingji() :
    print("第二题")
    qlist = [ random.randint(1,100) for i in range(1,11) ]
    plist = [random.randint(1, 100) for i in range(1, 16)]
    nlist = []
    for i in qlist :
        b = i not in nlist
        if b :
            nlist.append(i)
    for i in plist :
        b = i not in nlist
        if b :
            nlist.append(i)
    qlist.sort()
    plist.sort()
    print("qlist-->",qlist)
    print("plist-->",plist)

    nlist.sort()
    print(nlist)

def user() :
    print("第三题")
    while True:
        user = input("请输入用户信息")
        n = user.find("@")
        if n < 0:
            print("email邮箱格式不正确，缺少@符号")
        else:
            # 将用户姓名用切片返回出来
            muser = user[0:n]
            num = len(muser)
            if num >= 6:
                print("格式输入正确")
                break
            else:
                print("姓名长度不能小于6位")

def huiwen() :
    print("第四题")
    mstr = input("请输入一个字符串:")
    #for循环创建一个新的字符串
    nstr = ""
    for i in range(len(mstr)-1,-1,-1) :
        nstr+=mstr[i]
    if nstr == mstr :
        print("{0}是回文数".format(mstr))
    else :
        print("{0}不是回文数".format(mstr))
