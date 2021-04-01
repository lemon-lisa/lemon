'''
上节课回顾的注意点：文件要关闭，文件命名xlsx后缀名结尾的表格
'''
# ？？？行是和id有关系的
#  读数据的函数----嵌套字典的列表的测试用例[{用例1需要的数据}，{用例2需要的数据}]
#  参数{用例参数}执行的函数-----执行的结果----
#  写的函数-------依赖于执行结果和用例里面的期望值做比对
from lemon_day01.day05 import read_data,apitest,write

def test_fun(sheet):
    cases=read_data('test_case_api.xlsx',F'{sheet}')  #'''读取'''
    for case in cases:
        id=case['id']
        url=case['url']
        # print(url)
        data=eval(case['parm'])

        # print(type(data))
        expected=eval(case['expected'])
        '''
        {'code': 0, 'msg': 'OK'}
        '''
        res=apitest(url=url,param=data)
        print(res)
        '''
        {'code': 0, 'msg': 'OK',
         'data': {'id': 1000294837, 'reg_name': '34254sdfs', 'mobile_phone': '13552400101'},
         'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
        '''
        if res['msg'] == expected['msg']:
            finresult='passed'
        else:
            finresult = 'failed'
        write('test_case_api.xlsx',F'{sheet}',finresult,id+1,8)

# test_fun('login')
'''从excel读取出来的数据
整型：整型
字典/列表/元组：字符串
浮点：浮点
'''

'''eval() 对字符串里的某种数据格式返回他原本的数据类型，但是尽量不要对字符串这样操作'''
# 常用数据类型转换
'''eval在编程界时风险很大的方法'''

'''写的时候注意表单名
写要以字符串写入
在执行之前一定要把表格多余的部分删除
'''

'''======================UI自动化==============================='''
# 接口自动化最多，最稳定，性价比最高---回归
#  ui自动化不是很好做--不稳定  一对一的关系核心内容：找元素，操作（点击，切换，滑动）---冒烟
'''
人-----浏览器
代码胖胖（python）-----翻译（小卒）---浏览器(js)牛
翻译官：浏览器驱动，不同的浏览器驱动是不一样的
谷歌：chromdriver
火狐：geckodriver
ie:ieserverdriver

根据浏览器版本下载对应版本的驱动，最接近的，71版本向前兼容
selenium 安装和导入
1.ide---录制脚本
2.webdriver-----提供了一些对网页的操作办法
3.grid-----分布式，多个浏览器执行并发
'''
# from selenium import webdriver
# #初始化浏览器
# driver=webdriver.Chrome()
# driver.get('http://8.129.91.152:8765/Index/index')

'''selenium安装好
驱动下载----python的根目录
3，导入selenium
4,初始化一个浏览器
5.相关操作
'''

