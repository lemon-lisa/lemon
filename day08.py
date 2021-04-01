"""
手工冒烟测试
1.输入网址，看看他能不能正常打开网址
2.验证页面的标题，比如说验证下是否是柠檬erp
3.输入一个正常的用户名和密码，我验证下是否可以正常登录
4.判断下正常登录的用户名是不是叫测试用户
5.点击菜单能正常打开，比如我们这里的零售出库。
6.搜索单据的编号点击查询，判断查询出来的编号是对的
"""
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://erp.lemfix.com/login.html')
if driver.title =="柠檬ERP":
    print('获取标题测试通过')
else:
    print("测试不通过")
driver.find_element_by_id("username").send_keys('test123')

driver.find_element_by_id("password").send_keys('123456')

driver.find_element_by_id("btnSubmit").click()
import time

# time.sleep(10)
driver.implicitly_wait(10)
regname = driver.find_element_by_xpath("//p").text

if regname == "测试用户":
    print("判断用户名测试成功")
else:
    print("测试失败")

# 定位零售出库---点击   //span[text()="零售出库"]
driver.find_element_by_xpath('//span[text()="零售出库"]').click()
#定位单据编号输入框------输入查询数据//input[@name="searchNumber"]
time.sleep(5)
#TODO:如果嵌套子页面我要先切换
#1.找一下元素上面是否嵌套了html页面
#2.如果说出现了一个叫做iframe的名字，那么说明他是嵌套的
#3.switch_to的参数支持三种。索引，name(唯一标识id和name),frame的元素定位
#4.如果说像很长一串数字的这种一般是会变化的

# 先定位零售出库--找爸爸---拿id---拼接-frame
id=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute('id')
ele=driver.find_element_by_xpath(F'//iframe[@id="{id}-frame"]')
driver.switch_to.frame(ele)
time.sleep(2)
# print(F'//iframe[@id="{id}-frame"]')

# driver.switch_to.frame(F'{id}-frame')
# frame
driver.find_element_by_xpath('//input[@name="searchNumber"]').send_keys('877')

#定位查询------点击  //span[text()="查询"]
driver.find_element_by_xpath('//span[text()="查询"]').click()
#定位查询结果显示框----取出文本值
time.sleep(4)
text=driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]/td[@field="number"]/div').text
print('找到了')
#比对
if '877' in text :
    print('测试搜索成功')
else:
    print('测试失败')
driver.close()

# list1=driver.window_handles
# driver.switch_to.window()
# driver.switch_to.alert