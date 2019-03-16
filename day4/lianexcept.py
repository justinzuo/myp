
class YiChang(Exception) :
    print("差点报异常")

    def six(self):
        mstr = "我是自定义异常的six函数"
        print(mstr)

if __name__ == '__main__':
    #自己创建一个简易计算器
    num1 = int(input("请输入被除数:"))
    num2 = int(input("请输入除数:"))

    while True :
        # 将计算过程放进try内
        try:
            chu = num1 / num2
            print(chu)
        except ZeroDivisionError:
            print("除数不能为0")
        finally:
            break
    mstr = "12312"
    nstr = mstr[::-1]
    print(nstr)
    me = YiChang()
    try :
        raise YiChang()
    except YiChang :
        print("ojbk")
        me.six()
