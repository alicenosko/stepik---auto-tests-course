from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element_img = browser.find_element_by_id("treasure")
x = x_element_img.get_attribute("valuex")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

chekbox_robot = browser.find_element_by_id("robotCheckbox")
chekbox_robot.click()

radiobutton_robot = browser.find_element_by_id("robotsRule")
radiobutton_robot.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
