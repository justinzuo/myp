if __name__ == '__main__':
    mlist1 = [] #第一中创建列表的格式
    mlist2 = list() #第二种创建列表的格式

    mylist1 = []
    mylist2 =list()

    # print(type(mylist1))
    #     # print(type(mylist2))
    #     # mlist1.append("奥巴马") #append向列表尾部添加数据
    #     # print(mlist1)

    #     # mlist1.insert(0,"老鼠")
    #     # print(mlist1)
    #     # mlist2.insert(0,"葫芦娃") #insert(0)向下标为0的索引添加数据
    #     # mlist2.insert(5,"大洼")
    #     # print(mlist2)


    #     # mlist1.remove("老鼠") #删除指定的数据没有返回值,如果该数据不存在则抛出异常
    #     # print(mlist1)
    #     # del mlist1 #删除整个列表对象
    #     # del mlist2[0] #删除指定索引值的数据
    #     # print(mlist2)
    #     # print(mlist1) #由于删除了整个列表，所以不能打印数据
    mlist1.append("pig")
    mlist1.append("sheep")
    mlist1.append("targer")
    print("mlist1:",mlist1)
    rm = mlist1.pop(2) #pop()删除默认删除尾部数据，也可以指定索引，但是索引不能越界
    print("删除的是:"+rm)