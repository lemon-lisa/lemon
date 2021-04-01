import time
from selenium import webdriver
from lemon_day01.common.login import login
from lemon_day01.common.open_url import open_url
from lemon_day01.common.search import search
from lemon_day01.data.testcase import case


url=case.get('url')
username=case.get("username")
pwd=case.get('pwd')
num=case.get('num')

driver=webdriver.Chrome()

open_url(driver,url)
time.sleep(5)
login(driver,username,pwd)
time.sleep(5)
text=search(driver,num)

if num in text:
    print('测试搜索成功')
else:
    print('测试失败')

driver.close()