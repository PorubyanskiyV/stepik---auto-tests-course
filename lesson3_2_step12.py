import unittest
from selenium import webdriver
import time

class TestForInput(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        element = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        element.send_keys("Мой ответ")
        element2 = browser.find_element_by_xpath("// input[@placeholder='Input your last name']")
        element2.send_keys("Мой ответ2")
        element3 = browser.find_element_by_xpath("// input[@placeholder='Input your email']")
        element3.send_keys("Мой ответ3")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        element = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        element.send_keys("Мой ответ")
        element2 = browser.find_element_by_xpath("// input[@placeholder='Input your last name']")
        element2.send_keys("Мой ответ2")
        element3 = browser.find_element_by_xpath("// input[@placeholder='Input your email']")
        element3.send_keys("Мой ответ3")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
if __name__ == "__main__":
    unittest.main()