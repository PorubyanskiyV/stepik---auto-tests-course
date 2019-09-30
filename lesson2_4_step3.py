from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = " http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)
#time.sleep(1)
button = browser.find_element_by_css_selector("button.btn")
button.click()

message = browser.find_element_by_xpath("//div[@id='verify_message']")
assert "successful" in message.text

time.sleep(3)
# закрываем браузер после всех манипуляций
browser.quit()