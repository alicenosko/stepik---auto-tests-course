from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")
elements = browser.find_elements_by_tag_name('input')
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()