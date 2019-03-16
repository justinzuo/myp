# if __name__ == '__main__':
#     #创建列表并进行复核生成式
#     mlist = [i*i for i in range(1,11) ]
#     print("mlist-->",mlist)
#
#
#     mlist = []
#     for i in range(1,11) :
#         if i%2==0 :
#             mlist.append(i)
#     print("mlist-->",mlist)
#
#     mlist = [i for i in range(1,11) if i%2==0 ]
#     print("mlist-->",mlist)

# if __name__ == '__main__':
#     mlist = [1,2,3]
#     olist = ["a","b","c"]
#     nlist = []
#     for m in mlist :
#         for n in olist :
#             nlist.append(str(m)+n)
#     print("nlist-->",nlist)

# if __name__ == '__main__':
#     qlist = [1,2,3]
#     olist = ["a","b","c"]
#     mlist = [str(m) + n for m in qlist for n in olist ]
#     print("mlist-->",mlist)
#
#     dlist = [ i for i in range(1,11) if i%2!=0 ]
#
#     print("dlist-->",dlist)

# if __name__ == '__main__':
#     qlist = [1, 2, 3]
#     olist = ["a","b","c"]
#     mlist = [str(m) + n
#             for m in qlist \
#                 if m%2!=0 \
#             for n in olist ]
#     print("mlist-->",mlist)

if __name__ == '__main__':
    mlist = ["afde","das",123]
