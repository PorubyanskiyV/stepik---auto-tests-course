from selenium import webdriver
import time

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
#browser.implicitly_wait(5)
browser.get(link)
browser.find_element_by_id("button")
browser.quit()
###