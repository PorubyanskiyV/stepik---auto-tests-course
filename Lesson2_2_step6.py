from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)



x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

y_element = browser.find_element_by_xpath("//input[@id='answer']")
y_element.send_keys(y)

checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()

radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
radio.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
