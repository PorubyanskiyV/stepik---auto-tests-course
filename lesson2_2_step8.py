from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    element.send_keys("Мой ответ")
    element2 = browser.find_element_by_xpath("// input[@placeholder='Enter last name']")
    element2.send_keys("Мой ответ2")
    element3 = browser.find_element_by_xpath("// input[@placeholder='Enter email']")
    element3.send_keys("Мой ответ3")
####
    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла

    element = browser.find_element_by_xpath("//input[@id = 'file']")
    element.send_keys(file_path)







#####
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
#    time.sleep(1)

    # находим элемент, содержащий текст
 #   welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
 #   welcome_text = welcome_text_elt.text

#    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()