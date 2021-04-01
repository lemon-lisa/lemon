# 1、find 2、 _num 3、7val 4、add. 5、def 6、pan
# 7、-print 8、open_file 9、FileName
# 10、print 11、INPUT 12、ls 13、user^name 14、list1 15、str_

# name = input('请输入姓名：')
# age = input('请输入年龄：')
# gender = input('请输入性别：')
# # print('************')
# print('*' * 18)
# print(F'姓名:{name}')
# print(F'性别:{gender}')
# print(F'年龄{age}')
# print('*' * 18)
str1 = 'python hello aaa 123123aabb'
"""
     1）请取出并打印字符串中的'python'。 

     2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？ 

     3）找出字符串中字母‘a’的个数

     4) 找到aaa的起始位置 

     5）找到字母‘n’的索引
"""
# print(str1[0:6:1])
# print('o a' in str1)
# print(str1.count('a'))
# print(str1.find('aaa'))

# 列表  list  []
'''
1.没有元素就是空列表
2.可以存放任何数据类型,每个元素用逗号分隔  len  
3,元素能被改变，增删改  append是追加到末尾
'''

# print(list1)
# print(len(list1))
# print(list1[1])
# print(list1[1:3:1])
# print(list1[4][-1])
# # 增加
# list1.append('乔哥')
# print(list1)
# list1.insert(1,'邵名')
# print(list1)
# list2=['李瑞轩','欢喜']
# list1.extend(list2)
# print(list1)
# list1.insert(0,list2)
# # print(list1)

# 删除  pop  弹出
# list1 = [1,'胖胖','龙哥','小卒',['no longer','心灵治愈','小杨'],'胖胖']

# list1.pop(2)
#
# list1.clear()
#
# list1.remove('小卒')
# print(list1)
# 修改   先找到，赋值
# list1[1] = '李瑞轩'
# # print(list1)
# print(list1.count('胖胖'))
#  元组  tuple  ()最大的区别就是不可变，就是不支持增删改
# tuple1=(1,'胖胖','龙哥','小卒',['no longer','心灵治愈','小杨'])
# tuple2=list(tuple1)
# print(tuple2)
# tuple2[1]='李瑞轩'
# print(tuple2)
# tuple1=tuple(tuple2)
# print(tuple1)

# 字典  键值对，key:value    dict   {},每个元素也是用逗号隔开
#场景，描述物品的特性 一个人
#在3.6的版本以前他是无序的，没有索引的
# 不能重复  不可变的  key是不可变数据类型，value没要求，支持增删改
dict1={"name":"小卒","age":18,"high":175}
# print(dict1['gender'])   # 第一种取值方式,找不到报错
# print(dict1.get('gender'))   #找不到就返回None
#增加  指明key赋值
# dict1['gender']='女'
# print(dict1)
# dict1['name']='星光'   #  如果存在会覆盖值 就是修改
# dict1.pop("name")
# print(len(dict1))
# dict1.update({'city':'changsha','height':180})
# print(dict1)
#  集合  无序  set   {}   ,元素不可重复，去重
# set1={11,22,33,44,11,22}
# print(set1)
# list3=[11,22,33,44,11,22]
# print(set(list3))
# print(list(set(list3)))

#  控制流   if 判断 和for循环----空值代码的走向
# if 判断
# 如果我有一千万，那么我就取会所嫩模，如果我破产了，那么我就下海摸鱼了，
# 如果这两种都不是呢，我就安安心心学python

# if 判断会根据条件创建不同的分支,碰到冒号缩进，结果和条件他就是层级关系
# money = int(input('请输入金额'))
# if money>1000000 :
#     print('买房')
# elif money>100000:
#     print('买车')
# else:
#     print('种田')

# for 循环   重复执行某个代码，用来遍历某系数据对象的元素，字符串没列表，元组，字典
# for循环下面执行的代码叫做循环体
# 循环次数由元素的个数决定
#break   是终止循环跳出循环体不再继续循环
# continue 跳出本次循环，不会终止所有的循环
# 扩展知识点，range()    用来生成整数序列   []，
# 指定三个[开始，结束的位置，步长]，开始默认为0，步长默认为1

#  列表，字典进行循环
# str6='我爱柠檬班'
# print(len(str6))
# # 语法
# count=0
# for i  in str6:
#     if i == "柠":
#         continue
#     print(i)
#     count += 1
#     print(F'这是第{count}次打印')
# list4=range(0,11,1)---[0,1,2,3,4]
# print(list4)
# money=100

# for num  in range(0,11,1):
#     if num == 5:
#         pass
#     print(num)
#
#
#
#
#
#
#
# list6=['胖胖','龙哥','小卒','no longer','心灵治愈','小杨']
# for i in list6:
#     list6.remove(i)














