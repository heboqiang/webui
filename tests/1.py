from selenium import webdriver

driver = webdriver.Chrome()
base_url = "https://www.baidu.com"
driver.get(base_url)
d = driver.find_element_by_name("tj_trnews").click()