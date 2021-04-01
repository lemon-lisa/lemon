'''
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
3、list1 = ['胖胖','龙哥','小卒','no longer','心灵治愈','小杨']
 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
 并且把字典都存在新的 list中，最后打印最终的列表。--list2=[]
方法1： 手动扩充--字典--存放在列表里面；{} --简单
方法2： 自动--dict（）--不强制-- for循环 ，list2.append() --- 难度
4、for循环遍历其他的数据类型 --字典
5.列表list2 =['胖胖','龙哥','小卒','no longer','心灵治愈','小杨']
请用for循环结合列表删除方法remove执行删除元素，并说说你用remove的心得
'''
# a=[1,2,'6','summer']
# if 'i' in a:
#     print('在大家庭里面')
# else:
#     print('你不是我们家的人')

# dict_1={"class_id":45,'num':20}
# num=dict_1['num']
# print(num)
# if dict_1['num'] > 5 :
#     print(F'人数是{num}')
# else:
#     print('数量不达标')

# list1 = ['胖胖','龙哥','小卒','no longer','心灵治愈','小杨']
# pangpang={'name':'胖胖','age':18,'gender':'男'}
# longge={'name':'龙哥','age':18,'gender':'男'}
# list2=[]
# list2.append(pangpang)

# list2=[18,'男']
# #
# list3=[]
# for i in list1:
#     dict1=dict(name=i,gender=list2[-1],age=list2[0])
#     list3.append(dict1)
# print(list3)---等级最低的debug方式
import jsonpath as jsonpath

'''
1. 把字符串转成列表 - list() 
2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。
求里面所有数字的和 
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，
如果大于5，输出True；否则输出False。--if 判断嵌套 
'''
# len(数据)---参数
# def test(subject):
#     if  type(subject) ==list or type(subject) ==dict or type(subject) ==str:
#         if len(subject) >5:
#             print(True)
#         else:
#             print(False)
#     else:
#         print('输入的数据类型不正确')
#
# test('123')
# a='hello,lemon,lisa'
# list1=['hello','lemon','lisa']
# # print(list(a))
# #  split---字符串的方法:对字符串进行一个截断，返回列表
# #split有两个参数，1，以什么截取，2，截取多少次
# list2=a.split(',')
# print(list2)

#方法一  input  for  range
# num=int(input('请输入一个数字：'))

# for i in range(num):
#     sum+=i
# print(sum)

# def add(a):
#     sum = 0
#     for i in range(a):
#         sum += i
#     print(sum)

#==========================课堂内容========================
 #第三方库   使用：  1，要下载安装    2，导入
# requests 库  导入格式  import  导入的库名
#方法名实际上就是对应请求方式,requests参数除了url以外，其他都用字典
import requests

#注册接口
'''
1.请求方式：post
2，请求地址:http://8.129.91.152:8766/futureloan/member/register
3.请求参数的格式:json
4.请求头：是否需要传，传什么 X-Lemonban-Media-Type:lemonban.v2
Content-Type:application/json
5.是否需要依赖接口
'''
url='http://8.129.91.152:8766/futureloan/member/register'
param={
  "mobile_phone": "15815559988",
  "pwd": "lemon1234",
  "type":"0",
  "reg_name":"管理员用户lemon"
}
header={'X-Lemonban-Media-Type':'lemonban.v2',
        'Content-Type':'application/json'}
res=requests.post(url=url,json=param,headers=header)
# print(res.json())

# 登录
'''
1.请求方式：post
2，请求地址:http://8.129.91.152:8766/futureloan/member/login
3.请求参数的格式:json
4.请求头：是否需要传，传什么 X-Lemonban-Media-Type:lemonban.v2
Content-Type:application/json
5.是否需要依赖接口  不需要
'''
'''pprint  美化格式的功能'''
# url='http://8.129.91.152:8766/futureloan/member/login'
#
# param={
#   "mobile_phone": "15815555788",
#   "pwd": "lemon1234"
# }
# header={'X-Lemonban-Media-Type':'lemonban.v2',
#         'Content-Type':'application/json'}
# res=requests.post(url=url,json=param,headers=header)
# # print(res.json())  #  字典
# import pprint
# pprint.pprint(res.json())

# jsonpath   安装，导入----取出来的值是列表
# print(res.json()['data']['id'])
# print(res.json()['data']['token_info']['token'])
# import jsonpath
# id=jsonpath.jsonpath(res.json(),"$.data.id")[0]
# print(id)


# 充值
'''
1.请求方式：post
2，请求地址:http://120.78.128.25:8766/futureloan/member/recharge
3.请求参数的格式:json
4.请求头：是否需要传，传什么 X-Lemonban-Media-Type:lemonban.v2
Content-Type:application/json  token
5.是否需要依赖接口  需要  id   token
'''
# url='http://8.129.91.152:8766/futureloan/member/recharge'
# param={
#   "member_id": res.json()['data']['id'],
# #   "amount": "500000"
# # }
# # header={'X-Lemonban-Media-Type':'lemonban.v2',
# #         'Content-Type':'application/json','Authorization':F"Bearer {res.json()['data']['token_info']['token']}"}
# # res=requests.post(url=url,json=param,headers=header)
# # print(res.json())

#写思路     伪代码


def  abc():
    print('非常牛逼的功能')

def efg():
    print('函数2')