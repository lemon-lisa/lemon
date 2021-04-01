# a = [1,2,3,4,5]  #  2，4，5   2，4
# for i in a:
#     print()
# print(a)
# #   i值虽然是1，索引为0
# #   索引为1
# #  索引为2
# #  索引为3



# ;;;;;;;
# if ll..:
#
#相加
#  内置函数  ---都有自己的功能
# 一个函数就是一段代码，，这个代码代表某个功能----封装
#   def  函数名 ():
#       函数体   -------------才是能真正实现功能的代码
#函数要调用才会执行  函数名（）
# 用来提高代码的复用率
# 规矩：函数里面可能变化的内容不建议写在函数体里面---参数化
# 参数，
'''
1,必备参数，定义了就必须传，不传或者少传都会报错
2.默认参数：如果你有一些参数大概率使用的情况，
我们可以设置一个默认值，有默认值可以不传
3，不定长参数:不确定到底有没有，而且不确定有几个 *args   ,args是元组,只会接收多余的位置参数
    **kwargs:用字典取保存，只能传在后面
'''
# def add (a,b=100):   # 占位置的变量名叫做形参
#     # a = 10
#     # b = 20
#     sum = a + b
#     print(sum)
# add(10)   # 我们在调用的时候传的参数叫做实参
# '''此处是一万行代码
# '''
def job(salay,performance,bonus=200,*args,**kwargs):
    """
    :param salay: 基本工资
    :param bonus: 奖金
    :param performance: 绩效
    :return:
    """
    sum=salay+bonus+performance
    # print(F"salay is {salay}")
    # print(F"bonus is {bonus}")
    # print(F"args 是{args}")
    # print(F"kwargs 是{kwargs}")
    for i in args:
        sum +=i   # sum =sum +i
    for j in kwargs:
        sum +=kwargs[j]
    print(F"工资总和是{sum}")
    return sum ,salay



sum=job(2000,200,1000,400,aa=500,bb=600)
print(sum)
print(type(sum))

# 传参方式：位置传参--可能会出错
# 关键字传参：指定参数名进行传参，这种方式更精确，不容出错

#  返回值：函数执行后有数据需要给到调用的人使用，  ------sum
#  那么就把这个数据的变量设置成函数的返回值   -----返回sum
# 需要用到return的关键字，return后面跟你要返回的东西
# 如果说函数定义的返回值，我们用变量取接收函数的调用就是取接收返回值
# 返回值他的特点是什么呢返回值一定是在函数体的最后一行，后面的代码是不会被执行的
# 没有返回值的函数默认返回None  ，如果由多个返回值要用逗号隔开

# while 条件：
# # #     循环体
# 内置函数 print  len append  insert count type remove pop format clear del
# input range index find update

print('乔哥最帅'+'\n','胖胖次之')
