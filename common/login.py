def login(driver,username,pwd):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(pwd)
    driver.find_element_by_id("btnSubmit").click()
    # regname = driver.find_element_by_xpath("//p").text
    #
    # if regname == "测试用户":
    #     print("判断用户名测试成功")
    # else:
    #     print("测试失败")