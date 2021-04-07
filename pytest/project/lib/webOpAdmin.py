from selenium import  webdriver
from time import sleep
class webOpAdmin:
    def openBrowser(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self,username,password):

        self.driver.get("http://127.0.0.1/mgr/sign.html")

        if username is not None:
            self.driver.find_element_by_id("username").send_keys(username)
        if password is not None:
            self.driver.find_element_by_id("password").send_keys(password)

        self.driver.find_element_by_tag_name("button").click()
        sleep(1)

        alertText = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()

        return alertText

    def closeBrowser(self):
        self.driver.quit()

webopadmin = webOpAdmin()