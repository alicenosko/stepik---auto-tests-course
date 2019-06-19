import math

from selenium import  webdriver

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.trollface")
button.click()

new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

button_send = browser.find_element_by_css_selector("button.btn")
button_send.click()