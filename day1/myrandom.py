import random
# random.choice()随机选取参数中的子元素
if __name__ == '__main__':
    mstr = "abcdefghijklmn"
    # 临时存储
    tstr = ""
    #循环六次，取出六个字符
    for i in range(6) :
        v = random.choice(mstr)
        #拼接成字符串
        tstr+= v
    print(tstr)

random.shuffle将传入的参数的子元素随机打乱位置
if __name__ == '__main__':
    #创建一个列表
    ystr = ["zhenshi", "didi", "xingwei"]
    #shuffle会将传入的参数的子元素随机打乱位置，没有返回值
    random.shuffle(ystr)
    print("after {0}".format(ystr))

if __name__ == '__main__':
    #循环三次利用random.randint()中间传两个参数，取它们范围内的整数值
    for i in range(3) :
        i = random.randint(10, 20)
        print(i)

# random.uriform()使用
if __name__ == '__main__':
    i = 2
    j = 4
    #random.uniform()在里面传两个整形参数，返回这两个数范围内的浮点型数值
    val = random.uniform(i,j)
    print(val)

if __name__ == '__main__':
    i = 0
    j = 9
    val = random.randrange(i,j,3)
    print(val)