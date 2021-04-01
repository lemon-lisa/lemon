from selenium import webdriver
#初始化浏览器

"""
1.下载驱动放在对应的目录，他会启动一个exe文件,开启了一个服务
2，python---get()------driver（服务） -----返回了一个页面----接口请求
"""

"""
手工冒烟测试
1.输入网址，看看他能不能正常打开网址
2.验证页面的标题，比如说验证下是否是柠檬erp
3.输入一个正常的用户名和密码，我验证下是否可以正常登录
4.判断下正常登录的用户名是不是叫测试用户
5.点击菜单能正常打开，比如我们这里的零售出库。
6.搜索单据的编号点击查询，判断查询出来的编号是对的
"""
driver=webdriver.Chrome()
driver.get('http://erp.lemfix.com/login.html')
'''
获取标题，title-----特殊的属性
'''
if driver.title =="柠檬ERP":
    print('测试通过')
else:
    print("测试不通过")

"""
Html页面包含几部分
1.HTML-----基本上是定义页面呈现的内容，他是一个标签语言，
2.CSS------控制页面如何呈现，比如说我们的字体，颜色
3.JS------可以让页面在不同的情形下做不同的事情
div表示一块，input 输入的标签
属性是否唯一要根据开发决定，一般情况id和name唯一的
相关操作：点击  click   输入内容：send_keys    获取文本  text   获取属性attribute
"""
"""等待：页面跳转，切换，time"""
# 强制等待：time.sleep(10)----非常不智能
# 隐式等待：有一个默认的等待时间，等到元素出现直接继续执行，
#          一个会话只会执行一次，一般我们子啊浏览器打开后设置-----监视
# 显示等待-----自己取了解

#输入一个正常的用户名和密码
driver.find_element_by_id("username").send_keys('test123')

driver.find_element_by_id("password").send_keys('123456')

driver.find_element_by_id("btnSubmit").click()
import time
# time.sleep(10)
driver.implicitly_wait(10)
regname=driver.find_element_by_xpath("//p").text


if regname == "测试用户":
    print("测试成功")
else:
    print("测试失败")

"""浏览器常用操作"""
driver.close()      #关闭窗口
driver.quit()       #关闭浏览器
driver.minimize_window()  #最小化
driver.maximize_window()  # 最大化-----不最大化有可能定位不到边缘元素
driver.refresh()    #刷新
driver.forward()    #前进
driver.back()       #后退

"""xpath表达式----万能表达式"""

"""CSS和xpath有什么区别
1，CSS他查找代码更简洁
2.css他在谷歌 火狐 速度快一些，效率更高一些
3.css它不支持查找text
4.复杂元素查找xpath更简单
"""

# /html/body/div/div/div[1]/a/small----绝对路径，严格的顺序性
# # //small                           ----相对路径
#按住ctrl  +  f
# 父子关系可以使用单斜杠，其他隔代关系用双斜杠
"""
 //标签名[@属性名=属性值]
 //div[@class="login-logo"]//b  
 //b[text()="柠檬ERP"]
 //标签名[contains(@属性名/text(),属性值)]
 联合查找：//input[@id="username"and@name="username"]

"""

"""
一般找不到元素：1.表达式错误（ctrl+f验证）2.没等待
"""

