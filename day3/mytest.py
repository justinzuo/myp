
def radio1():
    print("欢迎来到腾讯氪金世界")

def radio2():
    print("本游戏唯一的规则就是：充钱你就会变强")

if __name__ == '__main__':
    b = True
    mlist = {}
    while b :
        print("1.登陆")
        print("2.注册")
        n = int(input("请输入选择:"))
        if n==1 :
            username = input("请输入用户名:")
            password = input("请输入密码:")
            while b:
                print("1.进入游戏")
                print("2.聊规则")
                print("3.退出程序")
                n = int(input("请输入选择"))
                if n == 1:
                    radio1()
                elif n == 2:
                    radio2()
                elif n == 3:
                    b = False
                    break
        elif n==2 :
            username = input("请输入用户名:")
            password = input("请输入密码:")
            mlist[username]=password