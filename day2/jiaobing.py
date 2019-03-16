
import random
if __name__ == '__main__':
    #先创建集合
    mset = { random.randint(1,10) for i in range(1,5) }
    nset = { random.randint(1,10) for i in range(1,5) }

    print("mset-->",mset)
    print("nset-->", nset)

    #差集,set1()-set2()返回第一个集合的元素在第二个集合里没有的元素
    cset = mset - nset
    print("cset-->",cset)

    #或运算 ,返回两个集合都有的元素并且按照升序排序
    hset = mset | nset
    print(type(hset))
    print("hset-->",hset)

    #与运算,只计算两个集合共同有的元素
    yset = mset & nset
    print("yset-->",yset)

    #A^B不同时包含于两个集合,返回不同时包含于两个集合内的元素
    gset = mset ^ nset
    print("gset-->",gset)

    num1 = len(mset)
    num2 = max(mset)
    #计算元素中的最大整数
    print(num2)

    for i in mset :
        #遍历mset集合
        print(i,end=" ")
    #.copy()复制集合返回新的集合
    eet=mset.copy()
    print("eet--》",eet)

    #.pop删除集合的第一个元素
    num = mset.pop()
    print("num-->",num)
    print(mset)