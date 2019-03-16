
#自定义异常
#这个类是继承子Exception(所有异常的父类)
class MyExcept (Exception) :
    pass

    def lady (self):
        print("异常里的lady()函数")
        mstr = input("请输入您的问题：")
        if mstr == "123" :
            print("抱歉，我无法处理您的问题")

if __name__ == '__main__':
    me = MyExcept()
    print("周天")
    try:
        #手动抛出异常
        raise MyExcept()
    except MyExcept :
        print("MyExcept异常")
        #调用了自定义异常的扩展函数
        me.lady()
    num1 = int(input("请输入第一个数字:"))
    num2 = int(input("请输入第二个数字:"))
    #捕获异常
    try :
        print(num1/num2)
    except ZeroDivisionError :
        print("除数不能为0")
    