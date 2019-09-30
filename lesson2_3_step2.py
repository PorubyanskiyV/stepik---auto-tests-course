from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

   # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(3)
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element_by_xpath("//input[@id='answer']")
    y_element.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
#    browser.quit()