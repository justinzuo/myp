
def laji():
    print("成功调用laji()函数")
def good():
    print("成功调用good()函数")
def pan (a,b):
    if a>b :
        print("{a}>{b}".format(a=a,b=b))
    elif a==b :
        print("{a}={b}".format(a=a, b=b))
    else :
        print("{a}<{b}".format(a=a, b=b))
def lkl (name = "laji",password= ""):
    print("{0}++{1}".format(name,password))
if __name__ == '__main__':
    good()
    laji()
    pan(int(input("请输入第一个数")),int(input("请输入第二个数")))
    lkl(name="shishui",password="1454")

def laji (mlist):
    mlist = [1,2,3,4,5,6]
    print("mlist-->",mlist)

mlist = ["a","b","s"]
laji(mlist=mlist)
print(mlist)

def myFunction (hun,cnt,val = "gundan" ):
    print(hun,cnt*val)
def gai (mlist):
    mlist = ["qwe","poi"]

if __name__ == '__main__':
    myFunction("dese",cnt=3)
    mlist = ["abc","sdc"]
    gai(mlist)
    print("mlist",mlist)

#函数形参元祖
def yuan (*myp):
    print(type(myp))
    print(myp)
    mlist = []
    for i in myp :
        mlist.append(i)
    return mlist

#字典形参
def zidian (**myp):
    #输出类型
    print(type(myp))
    print(myp)

if __name__ == '__main__':
    mlist = yuan("123","abc","name")
    print(type(mlist))
    print("mlist-->",mlist)
    mdict = zidian(name="zhangsan",age="13",sex="男")

def xiu (names):
    names.append("gun")
    names = ["589"]
    print(names)

if __name__ == '__main__':
    names = ["147", "acs", "axs"]
    xiu(names)
    print(names)
