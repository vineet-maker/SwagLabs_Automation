from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass

class LoginPage(BaseClass):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def login(self, username, password):
        self.wait_for_element(self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
