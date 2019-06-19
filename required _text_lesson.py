'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
 --- Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
 --- Нажать на кнопку "Забронировать"
 --- Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''

import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

button_send = browser.find_element_by_id("solve")
button_send.click()

# закрытие браузера
time.sleep(5)
browser.quit()


