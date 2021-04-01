import time


def search(driver,num):
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    time.sleep(5)
    id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute('id')
    ele = driver.find_element_by_xpath(F'//iframe[@id="{id}-frame"]')
    driver.switch_to.frame(ele)
    time.sleep(2)
    driver.find_element_by_xpath('//input[@name="searchNumber"]').send_keys(num)
    driver.find_element_by_xpath('//span[text()="查询"]').click()
    time.sleep(4)
    text = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]/td[@field="number"]/div').text
    return  text

