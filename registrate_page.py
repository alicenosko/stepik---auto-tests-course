from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
...
#first_name = browser.find_element_by_css_selector("input[placeholder='Введите имя']:required")
first_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")

first_name.send_keys("Ivan")
#last_name = browser.find_element_by_css_selector("input[placeholder='Введите фамилию']:required")
last_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")

last_name.send_keys("Petrov")
#email = browser.find_element_by_css_selector("input[placeholder='Введите Email']:required")
email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")

email.send_keys("i.petrov@gmail.com")

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
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
