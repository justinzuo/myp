import random
if __name__ == '__main__':
    mylist1 = ["1","2","5","3","9","4"]

    #sort()对列表进行永久性排序,默认排序规则是升序
    #先打乱列表顺序
    random.shuffle(mylist1)
    mylist1.sort()
    print(mylist1)
    #sort()如果参数为reverse=True 排序规则就会更改为降序
    mylist1.sort(reverse=True)
    print(mylist1)

    #打乱mylist1列表的顺序
    random.shuffle(mylist1)
    #sorted(,)临时排序，默认升序,有返回值
    print("sorted")
    mlist = sorted(mylist1)
    print(mlist)
    #临时排序，在第二个参数填入reverse=True就会变成降序
    print(sorted(mylist1,reverse=True))

    #reverse()反转列表的数据，不是对其进行排序！
    mylist2 = ["大娃","三娃","二娃","六娃"]
    mylist2.reverse()
    print("列表{0}".format(mylist2))

    alist = ["加里奥","锤石","派克","劫"]
    #clear()清空列表里的所有数据，但是会保留列表本身
    alist.clear()
    print("列表{0}".format(alist))