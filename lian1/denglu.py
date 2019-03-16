
mdict = {}
mlist = []

def denglu (username="",password="") :
    b = False
    for k,v in mdict.items() :
        if username==k and password==v :
            b =True
    if b :
        print("登录成功")
        return True
    else :
        print("登录失败")
        return False
def zhuce ():
    print("欢迎来到注册页面!")
    username = input("请输入您的用户名:")
    password = input("请输入您的密码:")
    mdict[username]=password
    print("注册成功")

def sleep () :
    while True:
        n = int(input("您确定要睡觉？输入1/2:"))
        if n == 1:
            print("请睡觉")
            mlist=+"sleep"
            break
        elif n == 2:
            print("那就不睡")
            mlist=+"not sleep"
            break
        else:
            print("输入不合法")

def eat (mstr) :
    print("{0}给你打包好了".format(mstr))
    mlist=+mstr

def dou () :
    print("抱歉，现在不支持打豆豆")

if __name__ == '__main__':
    b = True
    while b :
        print("1.登录")
        print("2.注册")
        print("0.退出程序")
        n = int(input("请输入选择"))
        if n == 1:
            username = input("请输入用户名:")
            password = input("请输入密码:")
            t = denglu(username=username, password=password)
            if t :
                while True :
                    print("1.看电影")
                    print("2.吃饭")
                    print("3.打豆豆")
                    print("0.退出登录")
                    n = int(input("请输入编号:"))
                    if n == 1 :
                        sleep()
                        print(mlist)
                    elif n==2 :
                        mstr = input("请输入吃什么:")
                        eat(mstr)
                        print(mlist)
                    elif n==3 :
                        dou()
                    elif n==0 :
                        print("退出登录")
                        break;
                    else :
                        print("输入不合法!")
            else :
                continue
        elif n == 2 :
            zhuce()
        elif n==0 :
            print("退出程序")
            break;
        else :
            print("输入不合法")