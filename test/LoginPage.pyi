from selenium.webdriver.common.by import By
from test import Locators

class LoginPage:
    def __init__(self,driver):
        self.txt_username = driver.find_element(By.ID, Locators.username_id)
        self.txt_password = driver.find_element(By.ID, Locators.password_id)
        self.btn_login = driver.find_element(By.XPATH, Locators.login_xpath)
        self.btn_create = driver.find_element(By.XPATH, Locators.create_new_xpath)

    def getTxtUser(self):
        return self.txt_username
    def getTxtPass(self):
        return self.txt_password
    def getLogin(self):
        return self.btn_login
    def getCreate(self):
        return self.btn_create