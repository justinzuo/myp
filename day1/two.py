if __name__ == '__main__':
    zifu1 = 'ilove'
    zifu2 = 'ILOVE'
    print(zifu1)
    print(zifu2)
    print(zifu1.title())
    zifu3 = '123'
    print(type(zifu3))
    zifu3 = int(zifu3)
    print(type(zifu3))
    mystrlist1 = ["good","good","good"]
    mystrlist2 = ["day","day","up"]
    for i in mystrlist1 + mystrlist2 :
        print(i , end= " ")
    else :
        print("\n没了")
    chuan = 'beijingkaoya'
    i = 0
    while i<chuan.__len__() :
        print(chuan[i],end=" ")
        i=i+1
    else :
        print("到头了")
    for i in mystrlist2 :
        pass
    myrange = range(9)
    for i in myrange :
        print(i,end="-")