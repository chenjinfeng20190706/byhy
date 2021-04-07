from selenium import  webdriver
from time import sleep
driver = None
def openBrowser():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

def login(username,password):
    global driver
    driver.get("http://127.0.0.1/mgr/sign.html")

    if username is not None:
        driver.find_element_by_id("username").send_keys(username)
    if password is not None:
        driver.find_element_by_id("password").send_keys(password)

    driver.find_element_by_tag_name("button").click()
    sleep(1)

    alertText = driver.switch_to.alert.text
    driver.switch_to.alert.accept()

    return alertText

def closeBrowser():
    global driver
    driver.quit()