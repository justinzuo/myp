# if __name__ == '__main__':
#     #预先准备好一个字符串
#     mstr = "you are my lady"
#     #find()默认查找该子串出现在字符串的第一次的位置，
#     # 第二个参数表示从指定索引位置开始查找
#     #第三个参数指定到该索引位置停止查找
#     #如果找不到该子串在字符串中的位置，那么将返回-1
#     i = mstr.find("lady",2,15)
#     print(i)

# if __name__ == '__main__':
#     mstr = "qw ert yu"
#     #index()函数，查找子串在源字符串中的位置
#     #第二个参数表示指定索引开始检索
#     #第三个参数表示指定索引停止检索,找不到该子串的位置就会报错
#     num = mstr.index("er",2,8)
#     print(num)

# if __name__ == '__main__':
#     mstr = "I really really really like"
#     #count()表示计数，在方法内第一个参数为子串查找该子串在源字符串出现了多少次
#     #第二个参数表示指定下标开始查找
#     #第三个参数表示指定下标结束查找
#     i = mstr.count("really",1,15)
#     print(i)

# if __name__ == '__main__':
#     mstr = "only man and only pig only sheep"
#     #replace()函数将源字符串内的元素替换
#     #第一个参数表示被替换子串，第二个表示替换的子串，
#     # 第三个参数为数值表示替换多少次，默认有多少被替换子串就替换多少次
#     # 该函数会返回一个新的字符串，不会更改源字符串
#     nstr = mstr.replace("only","just",3)
#     print(nstr)

# if __name__ == '__main__':
#     mstr = "good good study , day day up"
#     #split()函数会在源字符串中按指定传参切割字符串
#     #该函数会返回一个全新的字符串列表
#     #不填写参数会默认以空格、换行(\n)、制表符(\t)等进行切割
#     nstr = mstr.split(" ",2)
#     print(nstr)

# if __name__ == '__main__':
#     mstr = "u can u up, no zuo no die"
#     #capitalize()函数会将源字符串的首个字母大写返回一个新的字符串
#     nstr = mstr.capitalize()
#     print(nstr)