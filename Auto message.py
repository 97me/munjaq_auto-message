from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver.exe')

driver.get('http://munjaq.com/main')

driver.find_element_by_name('txtuserid').send_keys('ididid')
driver.find_element_by_name('txtuserpass').send_keys('pwdpwdpwd')
driver.find_element_by_xpath('//*[@id="btnlogin"]').click()

driver.find_element_by_xpath('/html/body/div/form/div/div[2]/div[1]/section[1]/div[3]/input[1]').click()

driver.find_element_by_name('message').send_keys('message message message')
