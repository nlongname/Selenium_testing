from selenium import webdriver
from selenium.webdriver.support.ui import Select

username = 'account'
password = 'password'

driver = webdriver.Firefox()
driver.get("http://www.mysticboards.us/forums/")
element = driver.find_element_by_name("user")
element.send_keys(username)
element = driver.find_element_by_name("passwrd")
element.send_keys(password)
select = Select(driver.find_element_by_name('cookielength'))
select.select_by_visible_text("Forever")
element = element.find_element_by_xpath("//input[@value='Login']").click()
