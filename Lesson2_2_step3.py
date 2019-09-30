from selenium import webdriver
import time
import math

#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)



num1 = browser.find_element_by_xpath("//span[@id='num1']")
x = num1.text

num2 = browser.find_element_by_xpath("//span[@id='num2']")
y = num2.text

sum = str(int(x)+int(y))

#expanding dropdown
#browser.find_element_by_tag_name('select').click()
#browser.find_element_by_css_selector("[value='43']").click()

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(sum)

button = browser.find_element_by_css_selector("button.btn")
button.click()
#
